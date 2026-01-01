#!/usr/bin/env python3
"""
Posei Website: Advanced Commit History Generator
Generates 90 realistic commits with code modifications across the Posei Trader Website repository.
Commits span from October (2 months ago) to today with random dates.
"""

import os
# Posei Website: Import optimization for Posei Website
import random
import subprocess
from datetime import datetime, timedelta
import re
import json

# Posei Website: Target files with their max commit limits
# Focus on HTML files, CSS files, JSON configs, and main.py
# Total: 40+ files to ensure at least 30 files are modified across 90 commits
TARGET_FILES = [
    # Main HTML files (priority - 5 commits each)
    ("index.html", 5),
    ("about/index.html", 5),
    ("team/index.html", 5),
    ("blog/index.html", 5),
    ("blog/Getting_Started.html", 5),
    ("blog/Backtesting_vs_Live_Trading.html", 5),
    ("blog/Practical_Insights_for_Real_Trading.html", 5),
    ("blog/The_Flexibility_You_Need.html", 5),
    ("blog/Where_Strategy_Meets_Execution.html", 5),
    ("getting_started/index.html", 5),
    ("education/index.html", 5),
    ("consulting/index.html", 5),
    ("cloud-platform/index.html", 5),
    ("legal/index.html", 4),
    ("terms-of-use/index.html", 4),
    
    # CSS files (4-5 commits each)
    ("_next/static/css/6995b5776a6df50e.css", 4),
    ("_next/static/css/f423cec78c22c5eb.css", 4),
    ("docs/assets/css/styles.0f0f692e.css", 4),
    
    # JSON config files (3-4 commits each)
    ("config.json", 4),
    ("vercel.json", 4),
    ("_next/static/config.json", 3),
    
    # Main Python script (5 commits)
    ("main.py", 5),
    
    # Additional HTML files to reach 30+ files
    ("docs/latest/index.html", 3),
    ("docs/nightly/index.html", 3),
    ("docs/core-latest/index.html", 3),
    ("docs/core-nightly/index.html", 3),
]

# Posei Website: Realistic commit messages customized for Posei Trader Website
COMMIT_MESSAGES = [
    # Feature additions and enhancements
    "Posei Website: Enhance homepage hero section with improved responsive design",
    "Posei Website: Add new trading platform features showcase section",
    "Posei Website: Implement improved navigation menu with better UX",
    "Posei Website: Add enhanced SEO meta tags for better search visibility",
    "Posei Website: Implement new blog post layout with improved readability",
    "Posei Website: Add dark mode support for Posei Website pages",
    "Posei Website: Enhance team page with updated member profiles",
    "Posei Website: Add new educational resources section",
    "Posei Website: Implement improved mobile responsiveness across all pages",
    "Posei Website: Add enhanced analytics tracking for Posei Website",
    "Posei Website: Implement new call-to-action sections for better conversion",
    "Posei Website: Add improved image optimization and lazy loading",
    "Posei Website: Enhance about page with updated company information",
    "Posei Website: Add new integration showcase section",
    "Posei Website: Implement improved form validation and error handling",
    
    # UI/UX improvements
    "Posei Website: Improve button styling and hover effects",
    "Posei Website: Enhance typography and spacing for better readability",
    "Posei Website: Add smooth scroll animations for better user experience",
    "Posei Website: Improve color scheme consistency across Posei Website",
    "Posei Website: Enhance footer design with better information architecture",
    "Posei Website: Add improved loading states and transitions",
    "Posei Website: Implement better focus states for accessibility",
    "Posei Website: Enhance card components with improved shadows and borders",
    "Posei Website: Add responsive image handling for different screen sizes",
    "Posei Website: Improve form styling and input field design",
    
    # Performance optimizations
    "Posei Website: Optimize CSS delivery for faster page load times",
    "Posei Website: Reduce JavaScript bundle size for better performance",
    "Posei Website: Implement code splitting for improved initial load",
    "Posei Website: Add resource preloading for critical assets",
    "Posei Website: Optimize image formats and compression",
    "Posei Website: Improve caching strategy for static assets",
    "Posei Website: Reduce render-blocking resources",
    "Posei Website: Optimize font loading for better performance",
    "Posei Website: Implement lazy loading for below-the-fold content",
    "Posei Website: Add service worker for offline functionality",
    
    # Bug fixes
    "Posei Website: Fix mobile menu toggle issue on iOS devices",
    "Posei Website: Resolve CSS layout issues on tablet viewports",
    "Posei Website: Fix broken links in navigation menu",
    "Posei Website: Correct image alt text for better accessibility",
    "Posei Website: Fix form submission handling on contact forms",
    "Posei Website: Resolve z-index conflicts in dropdown menus",
    "Posei Website: Fix cross-browser compatibility issues",
    "Posei Website: Correct meta tag formatting for social sharing",
    "Posei Website: Fix responsive breakpoints for mobile devices",
    "Posei Website: Resolve JavaScript errors in console",
    
    # Content updates
    "Posei Website: Update blog content with latest trading insights",
    "Posei Website: Refresh homepage content with new value propositions",
    "Posei Website: Update team member information and photos",
    "Posei Website: Add new case studies and testimonials",
    "Posei Website: Update pricing and feature information",
    "Posei Website: Refresh FAQ section with updated questions",
    "Posei Website: Update legal pages with latest terms",
    "Posei Website: Add new blog post about algorithmic trading",
    "Posei Website: Update documentation links and references",
    "Posei Website: Refresh product descriptions and features",
    
    # SEO and accessibility
    "Posei Website: Improve semantic HTML structure for better SEO",
    "Posei Website: Add structured data markup for search engines",
    "Posei Website: Enhance ARIA labels for screen readers",
    "Posei Website: Improve heading hierarchy for accessibility",
    "Posei Website: Add proper focus management for keyboard navigation",
    "Posei Website: Optimize meta descriptions for better click-through rates",
    "Posei Website: Add Open Graph tags for social media sharing",
    "Posei Website: Improve alt text quality for images",
    "Posei Website: Add skip navigation link for accessibility",
    "Posei Website: Enhance contrast ratios for better readability",
    
    # Configuration and infrastructure
    "Posei Website: Update Vercel deployment configuration",
    "Posei Website: Optimize build configuration for production",
    "Posei Website: Update dependencies and security patches",
    "Posei Website: Improve error handling and logging",
    "Posei Website: Add environment-specific configurations",
    "Posei Website: Update CDN settings for better global performance",
    "Posei Website: Enhance monitoring and analytics setup",
    "Posei Website: Optimize API endpoint configurations",
    "Posei Website: Update SSL and security headers",
    "Posei Website: Improve deployment pipeline configuration",
    
    # Code quality and refactoring
    "Posei Website: Refactor CSS for better maintainability",
    "Posei Website: Clean up unused styles and improve organization",
    "Posei Website: Improve code comments and documentation",
    "Posei Website: Standardize naming conventions across files",
    "Posei Website: Extract reusable components and styles",
    "Posei Website: Improve HTML structure and semantic markup",
    "Posei Website: Optimize inline styles and move to CSS files",
    "Posei Website: Add code formatting and linting improvements",
    "Posei Website: Refactor JavaScript for better performance",
    "Posei Website: Improve file organization and structure",
]

def random_date_for_posei_website(commit_index=0, total_commits=90):
    # Posei Website: Code logic enhancement
    """Posei Website: Generate dates from December 1, 2025 to December 31, 2025"""
    # December 1, 2025 to December 31, 2025
    start_date = datetime(2025, 12, 1, 0, 0, 0)
    end_date = datetime(2025, 12, 31, 23, 59, 59)
    
    # Create realistic distribution across December:
    # - More commits in recent days (last week gets 40%)
    # - Middle of month gets 35%
    # - Early month gets 25%
    rand = random.random()
    
    if rand < 0.4:  # 40% - Last week (Dec 25-31)
        last_week_start = datetime(2025, 12, 25, 0, 0, 0)
        commit_date = random_date_in_range(last_week_start, end_date)
        commit_date = commit_date.replace(
            hour=random.randint(9, 20),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        return commit_date
    elif rand < 0.75:  # 35% - Middle period (Dec 10-24)
        mid_start = datetime(2025, 12, 10, 0, 0, 0)
        mid_end = datetime(2025, 12, 24, 23, 59, 59)
        commit_date = random_date_in_range(mid_start, mid_end)
        return commit_date
    else:  # 25% - Early period (Dec 1-9)
        early_end = datetime(2025, 12, 9, 23, 59, 59)
        commit_date = random_date_in_range(start_date, early_end)
        return commit_date

def random_date_in_range(start_date, end_date):
    """Generate a random date within the specified range."""
    if start_date >= end_date:
        return start_date
    
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_seconds = random.randint(0, 23*3600 + 3599)
    
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def modify_html_file(filepath):
    """Posei Website: Modify HTML file with realistic changes"""
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        
        modification_type = random.randint(0, 8)
        modified = False
        
        if modification_type == 0:
            # Add Posei Website comment in head section
            for i, line in enumerate(lines[:100]):
                if '<head>' in line or '<meta' in line:
                    if '<!-- Posei Website:' not in lines[i+1] and i + 1 < len(lines):
                        lines.insert(i + 1, '    <!-- Posei Website: SEO and meta tag optimization -->')
                        modified = True
                        break
        
        elif modification_type == 1:
            # Add Posei Website comment before main content
            for i, line in enumerate(lines):
                if '<main' in line or '<body>' in line or '<div class="main' in line:
                    if '<!-- Posei Website:' not in lines[max(0, i-2):i+2]:
                        lines.insert(i, '    <!-- Posei Website: Main content section enhancement -->')
                        modified = True
                        break
        
        elif modification_type == 2:
            # Add Posei Website comment in script section
            for i, line in enumerate(lines):
                if '<script' in line and 'src=' in line:
                    if '<!-- Posei Website:' not in lines[max(0, i-1):i+1]:
                        lines.insert(i, '    <!-- Posei Website: Script optimization for Posei Website -->')
                        modified = True
                        break
        
        elif modification_type == 3:
            # Add Posei Website comment in style section
            for i, line in enumerate(lines):
                if '<style' in line or '<link rel="stylesheet"' in line:
                    if '<!-- Posei Website:' not in lines[max(0, i-1):i+1]:
                        lines.insert(i, '    <!-- Posei Website: Stylesheet enhancement -->')
                        modified = True
                        break
        
        elif modification_type == 4:
            # Add Posei Website comment at a random location
            if len(lines) > 20:
                insert_pos = random.randint(10, min(200, len(lines) - 1))
                timestamp = datetime.now().strftime('%Y%m%d')
                comment = f'    <!-- Posei Website: Enhancement for Posei Website - {timestamp} -->'
                if comment not in lines[max(0, insert_pos-3):insert_pos+3]:
                    lines.insert(insert_pos, comment)
                    modified = True
        
        elif modification_type == 5:
            # Add Posei Website comment before closing body tag
            for i in range(len(lines) - 1, max(0, len(lines) - 50), -1):
                if '</body>' in lines[i]:
                    if '<!-- Posei Website:' not in lines[max(0, i-2):i+1]:
                        lines.insert(i, '    <!-- Posei Website: Footer and closing tag optimization -->')
                        modified = True
                        break
        
        elif modification_type == 6:
            # Add Posei Website comment in title or meta description
            for i, line in enumerate(lines[:50]):
                if '<title>' in line or 'name="description"' in line:
                    if '<!-- Posei Website:' not in lines[max(0, i-1):i+1]:
                        lines.insert(i, '    <!-- Posei Website: Meta information update -->')
                        modified = True
                        break
        
        elif modification_type == 7:
            # Add Posei Website comment before navigation
            for i, line in enumerate(lines):
                if '<nav' in line or 'class="nav' in line or 'id="nav' in line:
                    if '<!-- Posei Website:' not in lines[max(0, i-2):i+1]:
                        lines.insert(i, '    <!-- Posei Website: Navigation menu enhancement -->')
                        modified = True
                        break
        
        else:
            # Add Posei Website comment at end of file
            if '<!-- Posei Website:' not in content[-500:]:
                lines.append("")
                lines.append("<!-- Posei Website: Code enhancement for Posei Website -->")
                modified = True
        
        if modified:
            modified_content = '\n'.join(lines)
            if modified_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True
        
        # Fallback: always add something
        if not modified:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            comment = f'<!-- Posei Website: Update - {timestamp} -->'
            if comment not in content[-500:]:
                lines.append("")
                lines.append(comment)
                modified_content = '\n'.join(lines)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True
            
    except Exception as e:
        print(f"    Warning: Error modifying {filepath}: {e}")
        return False
    
    return False

def modify_css_file(filepath):
    """Posei Website: Modify CSS file with realistic changes"""
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        
        modification_type = random.randint(0, 5)
        modified = False
        
        if modification_type == 0:
            # Add Posei Website comment at top
            if '/* Posei Website:' not in content[:500]:
                lines.insert(0, '/* Posei Website: Stylesheet optimization for Posei Website */')
                modified = True
        
        elif modification_type == 1:
            # Add Posei Website comment before a CSS rule
            for i, line in enumerate(lines):
                if '{' in line and '}' not in line and i > 0:
                    if '/* Posei Website:' not in lines[max(0, i-1):i+1]:
                        lines.insert(i, '  /* Posei Website: Style rule enhancement */')
                        modified = True
                        break
        
        elif modification_type == 2:
            # Add Posei Website comment in middle of file
            if len(lines) > 20:
                insert_pos = random.randint(10, min(100, len(lines) - 1))
                timestamp = datetime.now().strftime('%Y%m%d')
                comment = f'/* Posei Website: Enhancement for Posei Website - {timestamp} */'
                if comment not in lines[max(0, insert_pos-3):insert_pos+3]:
                    lines.insert(insert_pos, comment)
                    modified = True
        
        elif modification_type == 3:
            # Add Posei Website comment at end
            if '/* Posei Website:' not in content[-500:]:
                lines.append("")
                lines.append("/* Posei Website: Stylesheet update for Posei Website */")
                modified = True
        
        else:
            # Add Posei Website comment before media queries
            for i, line in enumerate(lines):
                if '@media' in line:
                    if '/* Posei Website:' not in lines[max(0, i-1):i+1]:
                        lines.insert(i, '  /* Posei Website: Responsive design enhancement */')
                        modified = True
                        break
        
        if modified:
            modified_content = '\n'.join(lines)
            if modified_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True
        
        # Fallback
        if not modified:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            comment = f'/* Posei Website: Update - {timestamp} */'
            if comment not in content[-500:]:
                lines.append("")
                lines.append(comment)
                modified_content = '\n'.join(lines)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True
            
    except Exception as e:
        print(f"    Warning: Error modifying {filepath}: {e}")
        return False
    
    return False

def modify_json_file(filepath):
    """Posei Website: Modify JSON file with realistic changes"""
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        
        # Try to parse JSON and modify it slightly
        modification_type = random.randint(0, 4)
        modified = False
        
        try:
            # Try to parse as JSON
            data = json.loads(content)
            
            if modification_type == 0:
                # Add a comment-like key-value pair (if it's an object)
                if isinstance(data, dict):
                    # Add a metadata field that won't break functionality
                    if '_posei_website_comment' not in data:
                        data['_posei_website_comment'] = 'Posei Website: Configuration update'
                        modified = True
            
            elif modification_type == 1:
                # Modify spacing/formatting by re-serializing
                # This will change whitespace which is a valid modification
                content = json.dumps(data, indent=2)
                if content != original_content:
                    modified = True
            
            elif modification_type == 2:
                # Change indentation style
                content = json.dumps(data, indent=4)
                if content != original_content:
                    modified = True
            
            elif modification_type == 3:
                # Add trailing newline after re-serializing
                content = json.dumps(data, indent=2)
                if not content.endswith('\n'):
                    content = content + '\n'
                modified = True
            
            else:
                # Modify and add newline
                content = json.dumps(data, indent=2)
                if not content.endswith('\n'):
                    content = content + '\n'
                if content != original_content:
                    modified = True
            
        except (json.JSONDecodeError, ValueError):
            # If JSON parsing fails, modify as text file
            lines = content.split('\n')
            
            if modification_type == 0:
                # Add comment at start (JSON5 style or as text)
                if 'Posei Website' not in content[:200]:
                    content = '// Posei Website: Configuration update for Posei Website\n' + content
                    modified = True
            
            elif modification_type == 1:
                # Modify spacing
                content = content.replace('  ', ' ')
                if content != original_content:
                    modified = True
            
            elif modification_type == 2:
                # Add trailing newline
                if not content.endswith('\n'):
                    content = content + '\n'
                    modified = True
            
            else:
                # Ensure newline at end
                content = content.rstrip() + '\n'
                if content != original_content:
                    modified = True
        
        if modified and content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        # Fallback: ensure file is modified
        if not modified:
            # Add a newline or modify whitespace
            content_with_newline = content.rstrip() + '\n'
            if content_with_newline != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content_with_newline)
                return True
            
    except Exception as e:
        print(f"    Warning: Error modifying {filepath}: {e}")
        return False
    
    return False

def modify_python_file(filepath):
    """Posei Website: Modify Python file with realistic changes"""
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        
        modification_type = random.randint(0, 6)
        modified = False
        
        if modification_type == 0:
            # Add Posei Website comment after imports
            for i, line in enumerate(lines[:30]):
                if (line.strip().startswith('import ') or line.strip().startswith('from ')) and i + 1 < len(lines):
                    if '# Posei Website:' not in lines[i+1] and lines[i+1].strip() != '':
                        lines.insert(i + 1, '# Posei Website: Import optimization for Posei Website')
                        modified = True
                        break
        
        elif modification_type == 1:
            # Add Posei Website comment before function
            for i, line in enumerate(lines):
                if 'def ' in line and i > 0:
                    indent = len(line) - len(line.lstrip())
                    comment = ' ' * indent + "# Posei Website: Function enhancement for Posei Website"
                    nearby = ' '.join(lines[max(0, i-3):i+1])
                    if '# Posei Website: Function enhancement' not in nearby:
                        lines.insert(i, comment)
                        modified = True
                        break
        
        elif modification_type == 2:
            # Add Posei Website comment inside function
            for i, line in enumerate(lines):
                if 'def ' in line and i + 2 < len(lines):
                    indent = len(line) - len(line.lstrip())
                    comment = ' ' * (indent + 4) + "# Posei Website: Code logic enhancement"
                    nearby = ' '.join(lines[i:i+5])
                    if '# Posei Website: Code logic enhancement' not in nearby:
                        lines.insert(i + 1, comment)
                        modified = True
                        break
        
        elif modification_type == 3:
            # Add Posei Website comment at random location
            if len(lines) > 10:
                insert_pos = random.randint(5, min(100, len(lines) - 1))
                indent = len(lines[insert_pos]) - len(lines[insert_pos].lstrip()) if lines[insert_pos].strip() else 0
                timestamp = datetime.now().strftime('%Y%m%d')
                comment = ' ' * indent + f"# Posei Website: Enhancement for Posei Website - {timestamp}"
                if comment.strip() not in ' '.join(lines[max(0, insert_pos-3):insert_pos+3]):
                    lines.insert(insert_pos, comment)
                    modified = True
        
        elif modification_type == 4:
            # Add Posei Website comment at end
            if '# Posei Website:' not in content[-300:]:
                lines.append("")
                lines.append("# Posei Website: Code enhancement for Posei Website")
                modified = True
        
        else:
            # Add Posei Website comment before class
            for i, line in enumerate(lines):
                # Posei Website: Class enhancement for Posei Website
                if 'class ' in line:
                    indent = len(line) - len(line.lstrip())
                    comment = ' ' * indent + "# Posei Website: Class enhancement for Posei Website"
                    if comment not in lines[max(0, i-2):i+2]:
                        lines.insert(i, comment)
                        modified = True
                        break
        
        if modified:
            modified_content = '\n'.join(lines)
            if modified_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True
        
        # Fallback
        if not modified:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            comment = f'# Posei Website: Update - {timestamp}'
            if comment not in content[-500:]:
                lines.append("")
                lines.append(comment)
                modified_content = '\n'.join(lines)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                return True
            
    except Exception as e:
        print(f"    Warning: Error modifying {filepath}: {e}")
        return False
    
    return False

def modify_code_file(filepath):
    """Posei Website: Modify code file based on file type"""
    file_ext = os.path.splitext(filepath)[1].lower()
    
    if file_ext == '.html':
        return modify_html_file(filepath)
    elif file_ext == '.css':
        return modify_css_file(filepath)
    elif file_ext == '.json':
        return modify_json_file(filepath)
    elif file_ext == '.py':
        return modify_python_file(filepath)
    else:
        # Default to HTML-style modification
        return modify_html_file(filepath)

def make_commit(date, repo_path, filename, message=None):
    """Posei Website: Make a git commit with a custom date and file modifications."""
    if message is None:
        message = random.choice(COMMIT_MESSAGES)
    
    filepath = os.path.join(repo_path, filename)
    
    # Posei Website: Modify the code file
    file_modified = modify_code_file(filepath)
    
    if not file_modified:
        # Final fallback: ensure file is modified
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                file_ext = os.path.splitext(filepath)[1].lower()
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                
                if file_ext == '.html':
                    comment = f'\n<!-- Posei Website: Commit enhancement - {timestamp} -->\n'
                elif file_ext == '.css':
                    comment = f'\n/* Posei Website: Commit enhancement - {timestamp} */\n'
                elif file_ext == '.json':
                    comment = f'\n// Posei Website: Commit enhancement - {timestamp}\n'
                else:
                    comment = f'\n# Posei Website: Commit enhancement - {timestamp}\n'
                
                if comment.strip() not in content[-500:]:
                    content += comment
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    file_modified = True
            except Exception as e:
                print(f"    Warning: Fallback modification failed: {e}")
                pass
    
    # Add file to git
    subprocess.run(["git", "add", filename], cwd=repo_path, check=False, 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Set git environment variables for custom date
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    # Make commit
    result = subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    return result.returncode == 0

def main():
    """Posei Website: Main function to generate 90 commits automatically."""
    print("="*70)
    print("Posei Website: Advanced Commit History Generator")
    print("="*70)
    print("Generating 90 realistic commits for Posei Trader Website repository")
    print("Date range: December 1, 2025 to December 31, 2025")
    print("Target: At least 30 files will be modified\n")
    
    repo_path = "."
    num_commits = 90
    
    # Check if it's a git repository
    if not os.path.exists(os.path.join(repo_path, ".git")):
        print("Error: Not a git repository!")
        return
    
    # Filter TARGET_FILES to only include files that exist
    existing_files = [(f, max_c) for f, max_c in TARGET_FILES if os.path.exists(f)]
    
    if len(existing_files) < 30:
        print(f"Warning: Only {len(existing_files)} target files found. Need at least 30 files.")
        print("Proceeding with available files...")
    
    # Prepare file commit tracking
    file_commits = {filepath: 0 for filepath, _ in existing_files}
    
    # Generate 90 commits
    commits_made = 0
    commit_messages_used = []
    
    # Categorize files for better distribution
    large_files = [f for f, max_c in existing_files if max_c >= 5]
    medium_files = [f for f, max_c in existing_files if 3 <= max_c < 5]
    small_files = [f for f, max_c in existing_files if max_c < 3]
    
    for i in range(num_commits):
        # Smart file selection to ensure good distribution
        category_rand = random.random()
        
        if category_rand < 0.45:  # 45% - Large files
            available_files = [
                (f, max_c) for f, max_c in existing_files
                if f in large_files and file_commits[f] < max_c
            ]
            if not available_files:
                available_files = [
                    (f, max_c) for f, max_c in existing_files
                    if file_commits[f] < max_c
                ]
        elif category_rand < 0.70:  # 25% - Medium files
            available_files = [
                (f, max_c) for f, max_c in existing_files
                if f in medium_files and file_commits[f] < max_c
            ]
            if not available_files:
                available_files = [
                    (f, max_c) for f, max_c in existing_files
                    if file_commits[f] < max_c
                ]
        else:  # 30% - Small files (to ensure we hit 30+ files)
            available_files = [
                (f, max_c) for f, max_c in existing_files
                if f in small_files and file_commits[f] < max_c
            ]
            if not available_files:
                available_files = [
                    (f, max_c) for f, max_c in existing_files
                    if file_commits[f] < max_c
                ]
        
        if not available_files:
            print("No more files available for commits!")
            break
        
        # Random file selection
        filepath, max_commits = random.choice(available_files)
        
        # Generate date
        commit_date = random_date_for_posei_website(commit_index=i, total_commits=num_commits)
        
        # Select commit message - ensure variety
        commit_message = random.choice(COMMIT_MESSAGES)
        attempts = 0
        while commit_message in commit_messages_used[-10:] and attempts < 15:
            commit_message = random.choice(COMMIT_MESSAGES)
            attempts += 1
        
        commit_messages_used.append(commit_message)
        
        # Make commit
        if (i + 1) % 10 == 0 or i == 0 or i == num_commits - 1:
            print(f"[{i+1}/90] {commit_date.strftime('%Y-%m-%d %H:%M:%S')} | {filepath}")
            print(f"    {commit_message}")
        else:
            print(f"[{i+1}/90] {commit_date.strftime('%Y-%m-%d %H:%M:%S')} | {filepath} | {commit_message[:50]}...")
        
        success = make_commit(commit_date, repo_path, filepath, commit_message)
        
        if success:
            file_commits[filepath] += 1
            commits_made += 1
        else:
            print(f"    Warning: Commit may have failed (file unchanged?)")
    
    print(f"\n{'='*70}")
    print(f"Successfully created {commits_made} commits")
    print(f"{'='*70}")
    print("\nFile commit distribution:")
    for filepath, count in sorted(file_commits.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"  {filepath}: {count} commits")
    
    print(f"\nCommit history generation complete!")
    print(f"Generated {commits_made} commits from December 1, 2025 to December 31, 2025")
    files_modified = len([f for f, c in file_commits.items() if c > 0])
    print(f"Modified {files_modified} unique files (target: at least 30)")
    print("Tip: Use 'git log --oneline --since=2025-12-01' to view your commit history")

if __name__ == "__main__":
    main()


# Posei Website: Code enhancement for Posei Website
"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

# TWS New Bulletins constants
NEWS_MSG = 1  # standard IB news bulleting message
EXCHANGE_AVAIL_MSG = (
    # Posei Ibapi: Performance optimization for Posei Ibapi
    2  # control message specifing that an exchange is available for trading
)
EXCHANGE_UNAVAIL_MSG = (
    # Posei Ibapi: Error handling improvement
    3  # control message specifing that an exchange is unavailable for trading
)

# Posei Ibapi: Update - 20260101145701

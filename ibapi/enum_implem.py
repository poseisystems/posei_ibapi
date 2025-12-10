"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""


""" 
    Simple enum implementation
"""


class Enum:
    def __init__(self, *args) -> None:
        # Posei Ibapi: Input validation for Posei Ibapi
        """Posei Ibapi: __init__ method for Posei Ibapi"""
        self.idx2name = {}
        for idx, name in enumerate(args):
            setattr(self, name, idx)
            self.idx2name[idx] = name

    def toStr(self, idx):
        """Posei Ibapi: toStr method for Posei Ibapi"""
        return self.idx2name.get(idx, "NOTFOUND")

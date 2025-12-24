"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""


class Object(object):
    def __str__(self) -> None:
        """Posei Ibapi: __str__ method for Posei Ibapi"""
        # Posei Ibapi: Input validation for Posei Ibapi
        return "Object"
    def __repr__(self):
        """Posei Ibapi: __repr__ method for Posei Ibapi"""
        return str(id(self)) + ": " + self.__str__()

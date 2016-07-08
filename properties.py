'''
Exploring the use of properties.

Flyweight Design Pattern
    Store the minimum information necessary.
    Everything else should be recalculated when needed.

__slots__
    turns off the ))dict)) to save memory.
    Use sparingly, don't repeat slots entries form a parent class.
'''

from __future__ import division
import validators

class PriceRange(object):

    __slots__ = ('_low', '_high')

    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        validators.is_positive(value)
        validators.is_number(value)
        self._low = value

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        validators.is_positive(value)
        validators.is_number(value)
        self._high = value

    @property
    def midpoint(self):
        return (self.high + self.low) / 2

    def recenter_around_midpoint(self, value):
        '''
        Recenter around new midpoint,
        keeping the distance the same
        '''
        distance = (self.high - self.low) / 2
        self.high = value + distance
        self.low = value - distance

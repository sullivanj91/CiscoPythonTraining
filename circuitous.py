'''
Copyright (c) 2016 Circuitous(tm)
All rights reserved.

Eric Ries, "Lean Startup Method"
YAGNI: Ya Ain't Gonna Need It

Agile : Waterfall :: Lean Startup : Business Plan
We are seeking product-market fit
(we have customers who buy stuff)

Inofrmation Hiding
    Principle of only providing what information
    is necessarey for the public interface.
    Keeping implementation details a secret,
    so you can change it without bothering anyone.

Bound Method
    instance.method()
    the instance automatically passes iself
    as the implicit first argument

Unbound Method
    Class.method()
    as instance method called from the class
    so you must pass the instance explictly

Static Method
    a function on a class that does not
    expect an instance as the first argument
    Useful for organizing your code in a large module.

Class Method
    Class.method()
    Automatically passes the class object
    as the first arguement. Useful for building
    alternate constructors.

Name Mangling
    self.__method()
    Methods starting with two underscores: ''__method''
    Are name-mangled so ''__Class__methdo'' to avoid
    accidental dependency injection by sublcasses.
    Good practice for any internal class dependencies.
    
'''

import math
from collections import namedtuple

Version = namedtuple('Version', 'major minor')

PI = math.pi

class Circle(object):
    'An advanced circle analytics toolkit'

    version = Version(0,8)

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_bdd(cls, diagonal):
        'build a circle from a bounding box diagnonal'
        radius = diagonal/(math.sqrt(2))
        return cls(radius)

    @property
    def radius(self):
        return self.diameter/2.0

    @radius.setter
    def radius(self, value):
        self.diameter = value * 2.0

    def __repr__(self):
        return '%s(radius=%r)' % (self.__class__.__name__, self.radius)

    def area(self):
        'Perform quadrature on a planar shape of uniform '
        radius = self.__perimeter()/(PI * 2)
        return PI * self.radius ** 2

    def perimeter(self):
        'Something really smart sounding...'
        return PI * self.radius * 2

    __perimeter = perimeter

    @staticmethod
    def angle_to_grade(angle):
        'Returns a percent grade given an inclinometer reading in degrees'

        return math.tan(math.radians(angle)) * 100
    

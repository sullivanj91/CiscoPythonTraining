'''
The customers' code, users of Circuitous(tm).
'''

from circuitous import Circle
from random import random, seed

# Customer 1: Our academic friends
print 'Proposal to research the areas of random circles'
print 'Using Circuitous(tm)', Circle.version
print 'The average area of 1000 random circles'
n = 1000
seed(42)
print 'seeded with the Answer to Life, the Universe...'
circles = (Circle(random()) for i in xrange(n))
areas = (c.area() for c in circles)
print 'is %.2f' % (sum(areas)/n)


# Customer 2: Local rubber sheet company
cuts = [0.7, 0.3, 0.5]
circles = [Circle(radius) for radius in cuts]
for c in circles:
    print 'a circle with radius', c.radius
    print 'has an area %.2f' % c.area()
    print 'and a perimeter %.2f' % c.perimeter()
    c.radius *= 1.1
    print 'and a warm area %.2f' % c.area()
    print

# Customer 3: Regional tire compnay

class Tire(Circle):

    def perimeter(self):
        'adjusted perimeter for width of tire'
        return Circle.perimeter(self) * 1.25

    __perimeter = perimeter

t = Tire(22)
print ' tire with radius 22'
print 'has an area %.2f' % t.area()
print 'and a perimeter %.2f' % t.perimeter()
print

# Customer 4: National Trucking Co.
print 'an incline of 7 degres'
print 'is a %d percent grade' % Circle.angle_to_grade(7)
print

# Customer 5: International Graphics Co.
print 'We have money and power'
print 'We build circles with counding boxes not radius'
c = Circle.from_bdd(10)
print 'a Circle with a bounding box diagonal 10'
print 'has a radius', c.radius
print 'and an area', c.area()
print

# Customer 6: Federal Government
# We like to micromanage!
# We will tell you not only WHAT to do
# But also HOW to do it

# ISO-fake1
# Thou shall not create area() methods that directly
# access the radius attribute. Instead, inside an area()
# method, thou shalt infer the radius from the perimeter.

# ISO-fake2
# Circle classes must not store the radius
# Circle classes must store the diameter ONLY

print 'federal inspection'
c = Circle(10)
print c.__dict__
print c.area()
print c.radius
c.radius = 20
print c.__dict__




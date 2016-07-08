'''
All about decorators

A ''def'' does 3 things:
    1. create a function object
    2. attach metadata (__name__, __doc__, ...)
    3. assign that object to a variable

Identity Function
    the output is the same as the input

Higher-Order Fuction
    either receives a funtion as input
    emits a function as ouput
    or both

Pure Function
    always returns the same output for a particular input
    and has no side-effects (only returns a value)

Wrapper Function
    uses a helper function
    typically outputs a similar result to the helper
    improving the behavior of the helper.

Factory Function
    makes and returns a new function

Closure
    Store a reference to local variables
    from the enclosing scope.
'''

import time
import math
import random

### Factory Functions ######################

def make_pow(exponent):
    def power(base):
        return base ** exponent
    return power

def make_logging(func):
    def logging_version(x):
        print 'calling %r' % func.__name__
        print 'with', x
        result = func(x)
        print 'resut was', result
        return result
    return logging_version

def make_caching(func):
    cache = {}
    def wrapper(x):
        if x in cache:
            return cache[x]
        result = func(x)
        cache[x] = result
        return result
    return wrapper

def random_cache(maxsize=128):
    def random_cache(func):
        cache = {}
        def wrapper(x):
            if x in cache:
                return cache[x]
            result = func(x)
            if len(cache) >= maxsize:
                del cache[random.choice(cache.keys())]
            cache[x] = result
            return result
        return wrapper
    return random_cache

### Wrapper Functions ######################

def logging_sin(x):
    print 'calling sin'
    print 'with', x
    result = math.sin(x)
    print 'resut was', result
    return result

def better_sqrt(x):
    'sqrt that works with negative inputs'
    if x >= 0:
        return math.sqrt(x)
    return math.sqrt(-x) * 1j

def logging_cos(x):
    print 'calling cos'
    print 'with', x
    result = math.cos(x)
    print 'resut was', result
    return result

def logging_tan(x):
    print 'calling tan'
    print 'with', x
    result = math.tan(x)
    print 'resut was', result
    return result

### Patching ##############################

import theirs

old_sqrt = math.sqrt

def patch_sqrt(x):
    'sqrt that works with negative inputs'
    if x >= 0:
        return old_sqrt(x)
    return old_sqrt(-x) * 1j

math.sqrt = patch_sqrt

print theirs.sqrts([81, -49, 4, 16])

### Higher-Order Functions #################

def identity(x):
    return x

registry = {}

def register(func):
    registry[func.__name__] = func
    return func

def add_docstring(func):
    if func.__doc__ is None:
        func.__doc__ = 'unknown documentation'
    return func

### Normal Functions #################

def square(x):
    return x * x

square = register(square)
square = add_docstring(square)
square = make_logging(square)

def cube(x):
    return x ** 3

cube = register(cube)
cube = add_docstring(cube)
cube = make_logging(cube)

def power(base, exponent=2):
    return base ** exponent

power = register(power)
power = add_docstring(power)

def collatz(x):
    'simple example of the halting problem'
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

collatz = register(collatz)
collatz = add_docstring(collatz)
collatz = make_logging(collatz)

@make_caching
def conjecture(x):
    'iterating collatz on itself shoud reach 1'
    while x != 1:
        x = collatz(x)
    return True

cache = {}

def caching_conjecture(x):
    if x in cache:
        return cache[x]
    result = conjecture(x)
    cache[x] = result
    return result 

@random_cache
@make_logging
def hardwork(x):
    'simulate doing hard work'
    print 'doing hard work'
    time.sleep(1)
    return x + 1

cache = {}

def caching_hardwork(x):
    'do hard work, but remember past results'
    if x in cache:
        return cache[x]
    result = hardwork(x)
    cache[x] = result
    return result












'''
Some useful validators
'''

def is_positive(value):
    if value < 0:
        raise ValueError('expected positve got %r' % value)
    return True

def is_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError('expected an int or float, got %r' % value.__class__.__name__)
    return True
                

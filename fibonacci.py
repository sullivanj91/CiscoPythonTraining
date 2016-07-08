'''
The Classic Fibonacci Sequence.
'''

import decorators

def nth(n):
    'Iterative version of fib'
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

@decorators.make_caching
def nth(n):
    '''
    The n-th number in the Fibonacci sequence.
        0: 0
        1: 1
        n: (n-1)th + (n-2)th
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth(n-1) + nth(n-2)

def sequence(n):
    'The first n numbers in the Fibonacci sequence'
    for i in range(n):
        print nth(i)

if __name__ == '__main__':
    import sys
    n = 10
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    sequence(n)

'''
A basic testing framework
'''

### module.py ###################

def square(x):
    return x ** 2

def collatz(x):
    if x % 2 == 0:
        return x//2
    return 3 * x + 1


### framework.py ###############

registry = []

def test(func):
    registry.append(func)
    return func

def run():
    for func in registry:
        try:
            func()
        except AssertionError:
            print 'FAILED: %r' % func.__name__
        else:
            print 'PASSED: %r' % func.__name__
            
### test_module.py ##############

# import module
# from framework import run

@test
def square_case_5():
    assert 25 == square(5)

@test
def collatz_case_5():
    assert 16 == collatz(5)

if __name__ == '__main__':
    run()

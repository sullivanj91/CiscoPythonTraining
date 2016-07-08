'''
Creating deadlock,
then solving.
'''

from threading import Lock, Thread
import random

class Account:
    '''
    Changing the value in an account should only be done
    by an acct.transfer() which ensures no double-spending.
    '''

    def __init__(self, name, value):
        self.name = name
        self._value = value
        self.lock = Lock()

    def __repr__(self):
        return 'Account(%r, %r)' % (self.name, self.value)

    @property
    def value(self):
        return round(self._value, 2)

    def transfer(self, other, amount):
        '''
        lock both accounts during transfer
        and verify that neither will be over-drafted
        '''
        # order the locks to avoid deadlock
        if self.name < other.name:
            lower, higher = self, other
        else:
            lower, higher = other, self
        
        with lower.lock, higher.lock:
            if self.value - amount < 0:
                raise ValueError('OVERDRAFT: %r' % self)
            if other.value + amount < 0:
                raise ValueError('OVERDRAFT: %r' % other)
            self._value -= amount
            other._value += amount


def worker(name):
    for i in range(10):
        a,b = random.sample(accounts, 2)
        amount = round(random.random(), 2)
        print '%r: %r from %r to %r' % (name, amount, a, b)
        a.transfer(b, amount)
        #print 'DONE %r: %r from %r to %r' % (name, amount, a, b)
        
            
if __name__ == '__main__':
    accounts = [Account(name, 10) for name in 'abc']
    threads = [Thread(target=worker, args=(i,)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


    

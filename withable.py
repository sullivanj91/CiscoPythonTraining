'''
The greatest invention since the sub-routine!

Operator        Magic Method        Vocabulary

+               __add__             addable
/               __div__             divisible
len             __len__             sizable
[]              __getitem__         indexable
for             __iter__            iterable
next()          next                iterator
with            __exit__            context manager
'''

import sys

class ContextManager:
    'A generic context manager'

    def __init__(self, value):
        self.value = value

    def __exit__(self, etype, einstance, etraceback):
        print 'leaving the conext'
        print etype
        print einstance
        print etraceback
        if etype == TypeError:
            print 'handling the error'
            return True

    def __enter__(self):
        print 'entering the context'
        return 42

with open('notes/hamlet.txt') as f:
    text = f.read()

import threading
lock = threading.Lock()


# The old way
try:
    lock.acquire()
    print 'critical section'
    print 'using a shared resource'
finally:
    lock.release()

# New Pythonic way
with lock:
    print 'critical section'
    print 'using a shared resource'

class File:
    'paraphrasing file type'

    def __init__(self, filename):
        self.fp = 'use the os'

    def __iter__(self):
        return self

    def next(self):
        return 'next line in the file'

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        print 'use the os'

class Closing:

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, etype, einstance, etraceback):
        self.obj.close()

class Ignore(object):

    def __init__(self, *args):
        self.etypes = args

    def __enter__(self):
        return self

    def __exit__(self, etype, einstance, etraceback):
        if etype in self.etypes:
            return True

class RedirectStdout(object):
    'example of robust dependecy injection'

    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.target

    def __exit__(self, etype, e, tb):
        sys.stdout = self.old_stdout


if __name__ == '__main__':
    cm = ContextManager(4)
    with cm as value:
        print 'inside the context'
        print 'value is', value
        print 1 + '1'
        print 'completing the context'

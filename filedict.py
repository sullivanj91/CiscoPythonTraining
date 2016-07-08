'''
build a dict-like object, backed by the filesystem
It will have the same interface as a readl dictionary
But will gain the benefites of the filesystem

    - persistence
    - concurrency
    - introspectable
    - shareable with other language
'''

from collections import MutableMapping
import os, pickle

class FileDict(MutableMapping):
    'dict-lik, backed by the filesystem'
    #filename is the key
    #file data is the value

    def __init__(self, dirpath, *args, **kwargs):
        self.dirpath = dirpath
        try:
            os.mkdir(dirpath)
        except OSError:
            pass #ignore, dictionary already exits
        self.update(*args, **kwargs)

    def __setitem__(self, key, value):
        filename = os.path.join(self.dirpath, key)
        with open(filename, 'wb') as f:
            pickle.dump(value, f)

    def __getitem__(self, key):
        filename = os.path.join(self.dirpath, key)
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def __delitem__(self, key):
        filename = os.path.join(self.dirpath, key)
        try:
            os.remove(filename)
        except OSError:
            raise KeyError(key)

    def __iter__(self):
        return iter(os.listdir(self.dirpath))

    def __len__(self):
        return len(os.listdir(self.dirpath))

    def __repr__(self, *args, **kwargs):
        return '%s(%r, %r)' % (self.__class__.__name__, self.dirpath,
                               self.items())
        
if __name__ == '__main__':
    d = FileDict('starwars')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth'

    print d
    d['hero'] = ('Rey', 'Finn')
    del d['villain']

    print d
    print len(d)

'''
Using dict.__missing__
'''

class AngryDict(dict):

    def __missing__(self, key):
        print 'I am so angry!', key, 'is missing.'
        raise KeyError(key)

class ZeroDict(dict):

    def __missing__(self, key):
        return 0

class ListDict(dict):

    def __missing__(self, key):
        value = []
        self[key] = value
        return value

class ChainDict(dict):

    def __init__(self, fallback, *args, **kwargs):
        self.fallback = fallback
        self.update(*args, **kwargs)

    def __missing__(self, key):
        return self.fallback[key]


defaults = {'bg':'black', 'fg':'green', 'h':24, 'w':80}
settings = ChainDict(defaults, {'fg':'cyan', 'h': 40})

# ChainDict parallels how attribute lookups work
#   instance --> class --> bases --> AttributeError
# and how imports work
#   current directory --> PYTHONPATH --> site-packages --> install folders
# and how variable lookup work:
#   locals() --> globals --> __builtins__ --> NameError

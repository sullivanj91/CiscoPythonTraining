'''
A discussion of abstract Base classes

Mixins are GREAT!
    programming becomes as easy as
    writing alist of capabilities

Mixins are also TERRIBLE!
    you might accidentally instantiate the mixin
    you might forget to implement the requirements in a subclass

Abstract Base Classes (ABCs) to the rescue!
    An ABC is like a prefabricated building
    you pour the foundation with the subclass.
    If you make the right connections,
    you can place the ABC on top and get
    a lot of features built quickly.

    An ABC is like a contract:
    - you must override the required abstract methods
    - if you do, you gaoin nome nice mixed in features
'''
from abc import abstractmethod, ABCMeta
from collections import Sequence


class Capper(Sequence):

##    __metaclass__ = ABCMeta
    
    def capitalize(self):
        return ''.join([s.upper() for s in self])

##    @abstractmethod
##    def __getitem__(self, index):
##        return None
##
##    @abstractmethod
##    def __len__(self):
##        return 0

class Uncapper:

    __metaclass__ = ABCMeta

    def uncapitalize(self):
        return ''.join([s.lower() for s in self])

    @abstractmethod
    def __getitem__(self, index):
        return None

    @abstractmethod
    def __len__(self):
        return 0

class SkipSeq(Capper, Uncapper):
    '''
    a sequece that skips every other index

        >>> skip = SkipSeq('abcde')
        >>> skip[0]
        'a'
        >>> skip[1]
        'c'
        >>> skip[2]
        'e'
        >>> len(skip)
        3
    '''

    def __init__(self, seq):
        self.seq = seq

    def __getitem__(self, index):
        return self.seq[index * 2]

    def __len__(self):
        return (len(self.seq) + 1) // 2


class WordSeq(Capper, Uncapper):
    '''
    turns a sentence into a sequence of words

        >>> words = WordSeq('hello world')
        >>> words[0]
        'hello'
        >>> words[1]
        'world'
    '''

    def __init__(self, sentence):
        self.words = sentence.split()

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)


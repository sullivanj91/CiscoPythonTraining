from collections import deque
from collections import defaultdict
from random import choice

class WordChain:
    'Markav chain of words'

    def __init__(self, size):
        self.size = size
        self.chain = defaultdict(list)

    def build(self, filename):
        previous = deque(maxlen=self.size)
        with open(filename) as f:
            for line in f:
                for word in line.split():
                    self.chain[tuple(previous)].append(word)
                    previous.append(word)

    def replay(self):
        previous = deque(choice(self.chain.keys()), maxlen=self.size)
        print previous
        while previous[-1][-1] not in '.?!':
            word = choice(self.chain[tuple(previous)])
            print word,
            previous.append(word)

if __name__ == '__main__':
    chain = WordChain(2)
    chain.build('notes/hamlet.txt')
    chain.replay()

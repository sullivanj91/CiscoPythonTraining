'''
Using a lock to avoid a race condition
'''

### SERIAL VERSION ######################

from collections import Counter, deque

counts = Counter()

with open('notes/hamlet.txt') as f:
    for line in f:
        for word in line.split():
            counts[word] += 1

print 'SERIAL, CORRECT COUNT'
print 'most common 3 words'
print counts.most_common(3)
print

### THREADED VERSION ##################

import threading
from Queue import Queue

q = Queue()
counts = Counter()
lock = threading.Lock()

def parse_words(filename):
    with open(filename) as f:
        for line in f:
            for word in line.split():
                q.put(word)

##def count_words():
##    while q:
##        try:
##            word = q.popleft()
##        except IndexError:
##            pass
##        else:
##            with lock:
##                counts[word] += 1

def count_words():
    while q:
        word = q.get()
        with lock:
            counts[word] += 1
        q.task_done()


filenames = ['notes/hamlet.txt', 'notes/nasa.log.sample']
producers = [threading.Thread(target=parse_words, args=(name,)) for name in filenames]
for t in producers:
    t.start()

workers = [threading.Thread(target=count_words) for i in range(10)]
for t in workers:
    t.daemon = True #Kill subthreads whe main thread dies
    t.start()

for t in producers:
    t.join()
q.join()

print 'THREADED VERSION'
print 'most common 3'
print counts.most_common(3)
print

### EASY THREADING #######################

from multiprocessing.pool import ThreadPool
from itertools import chain

counts = Counter()
lock = threading.Lock()

def parse_words(filename):
    words = []
    with open(filename) as f:
        for line in f:
            for word in line.split():
                words.append(word)
    return words

def count_words(words):
    for i, word in enumerate(words):
        with lock:
            counts[word] += 1
    return i

producers = ThreadPool(2)
wordlists = producers.imap_unordered(parse_words, filenames)

consumers = ThreadPool(2)
total = sum(consumers.imap_unordered(count_words, chain(wordlists)))

print 'EASY THREADING'
print counts.most_common(3)
print 'total words counted:', total










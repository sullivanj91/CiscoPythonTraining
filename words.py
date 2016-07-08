import collections


#Task 1: Count the frequency of words in Hamlet
counts = {}
with open('notes/hamlet.txt') as f:
	for line in f:
		for word in line.split():
			counts[word] = counts.get(word, 0) + 1

print sorted(counts.items(), key=lambda p: p[1], reverse=True)[:3]

#collections.Counter provides 2 features: .get(key, 0)
counts = collections.Counter()
with open('notes/hamlet.txt') as f:
        for line in f:
                for word in line.split():
                        counts[word] += 1

print counts.most_common(3)

#Task 2: Organize the unique words by first letter
#       show all the words that start with 'v'

uniques = {} # dict of first letters --> set of words starting with that letter
with open('notes/hamlet.txt') as f:
        for line in f:
                for word in line.split():
                        first_letter = word[0]
                        uniques.setdefault(first_letter, set()).add(word)

uniques = collections.defaultdict(set)
with open('notes/hamlet.txt') as f:
        for line in f:
                for word in line.split():
                        first_letter = word[0]
                        uniques[first_letter].add(word)


#Task 3: Build a dict of lists
#        keys are each word
#        values are a list of all the words that
#        have come immediately after that key

chain = collections.defaultdict(list)
size = 3
previous = collections.deque(maxlen=size)
with open('notes/hamlet.txt') as f:
        for line in f:
                for word in line.split():
                        chain[tuple(previous)].append(word)
                        previous.append(word)

import random

previous = collections.deque(random.choice(chain.keys()), maxlen=size)
print previous,

while previous[-1][-1] not in '.?!':
        word = random.choice(chain[tuple(previous)])
        print word,
        previous.append(word)





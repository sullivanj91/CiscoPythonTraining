'''
Authentication -- username/password
'''

import hashlib

passwords = {}

def store_password(username, password):
    passwords[username] = password

def check_password(username, password):
    return passwords[username] == password

### One-Way Transformation ######################

def store_password(username, password):
    passwords[username] = hash(password)

def check_password(username, password):
    return passwords[username] == hash(password)

### The Good Way ##########################

import string
import random

pop = string.ascii_letters + string.digits

def good_password(n=20):
    return ''.join(random.choice(pop) for i in range(n))

salt = good_password()

def store_password(username, password):
    passwords[username] = hashlib.sha512(password + salt).hexdigest()

def check_password(username, password):
    return passwords[username] == hashlib.sha512(password + salt).hexdigest()

### Test Data ############################

crummy_passwords = '''
michael superman password 1234 hello bobby
cisco cisco123 admin root'''.split()

for i, password in enumerate(crummy_passwords):
    username = 'User%03d' % i
    store_password(username, password)

### Hacker: Rainbow Table ################

rainbow = {} # hashcoe --> password

with open('notes/common_passwords.txt') as f:
    for line in f:
        password = line.split(', ')[0]
        hashcode = hashlib.sha512(password).hexdigest()
        rainbow[hashcode] = password



### A Better Hash #########################

import md5

def store_password(username, password):
    passwords[username] = md5.new(password).hexdigest()

def check_password(username, password):
    return passwords[username] == md5.new(password).hexdigest()

### A Better Hash? #########################

import hashlib

def store_password(username, password):
    passwords[username] = hashlib.sha512(password).hexdigest()

def check_password(username, password):
    return passwords[username] == hashlib.sha512(password).hexdigest()


### Hacker: Brute-Force ######################

# 1. What if they know something about our hashng algo?
# 2. What if they know a bunch of common passwords?

if __name__ == '__main__':
    store_password('luggage', '12345')
    print check_password('luggage', '12345')
    print check_password('luggage', 'wrong')

    for username, hashcode in passwords.items():
        if hashcode in rainbow:
            print 'Gotcha! %r: %r' % (username, rainbow[hashcode])

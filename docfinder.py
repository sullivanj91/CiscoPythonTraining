'''
Keyword-searchable document database.

API:
    add_document(uri, content) --> None
    get_document(uri) --> content of that document
    search(keyword0, keyword1,... keywordN) --> list of document uris
                                                in order of relevance
    Exceptions: UnknownURI, DuplicateURI

Tables:
    Documents                                   Keywords
    ----------------                            -------------------
    uri         text <-- unique index           uri         text
    content     blob                            term        text <-- index
                                                score       real

'''

from __future__ import division
from collections import Counter
from contextlib import closing
import sqlite3, re, os, bz2

import argparse, sys

__all__ = ['search', 'add_document', 'get_document', 'UnknownURI', 'DuplicateURI']

database = 'pepsearch.db'

stopwords = {'and', 'or', 'the', 'of', 'a'}

class UnknownURI(Exception):
    'URI not present in database'

class DuplicateURI(Exception):
    'URI not present in database'

def normalize(words):
    '''
    Lowercases, removes plurals, and ignores stopwords
    to improve caparablility of search terms.
    '''
    normalized = []
    for word in words:
        word = word.lower()
        word = word.rstrip('s')
        if word not in stopwords:
            normalized.append(word)
    return normalized

def score_document(text, pattern=r'[A-Za-z]+', n=200):
    '''
    Calculate the term-relevance scores
    for the ''n'' most-frequent words in the text.
    '''
    # normalize words before scoring

    scores = []
    counter = Counter()
    words = re.findall(pattern, text)
    total = len(words)
    words = normalize(words)
    counts = Counter(words).most_common(n)

    return ((word, count/total) for word, count in counts)

def create_db(force=False):
    'Create database, delete existing if ''force'' == True'
    if force:
        try:
            os.remove(database)
        except OSError:
            pass
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute('CREATE TABLE Documents (uri text, content blob)')
        c.execute('CREATE TABLE Keywords (uri text, term text, score real)')
        c.execute('CREATE UNIQUE INDEX uriIndex ON Documents (uri)')
        c.execute('CREATE INDEX termIndex ON Keywords (term)')
        

def add_document(uri, contents):
    '''
    Insert a new document into the database with the specified URI.
    Raises DuplicateURI if URI already exits in the database.
    '''
    blob = sqlite3.Binary(bz2.compress(contents))
    try:
        with closing(sqlite3.connect(database)) as connection:
            c = connection.cursor()
            c.execute('INSERT INTO Documents VALUES (?, ?)', (uri, blob))
            args = ((uri, term, score) for term, score in score_document(contents))
            c.executemany('INSERT INTO Keywords VALUES (?, ?, ?)', args)
            connection.commit()
    except sqlite3.IntegrityError:
        raise DuplicateURI(uri)

def get_document(uri):
    '''
    Return the text of the document in the database
    that matches the specified URI.

    Raises UnknownURI if URI not found in the database
    '''
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute('SELECT content FROM Documents WHERE uri=?', (uri,))
        row = c.fetchone()
        if row is None:
            raise UnknownURI(uri)
        return bz2.decompress(row[0])
        

search_query_template = '''\
SELECT uri
FROM Keywords
WHERE term IN (%s)
GROUP BY uri
ORDER BY sum(score) DESC
'''

def search(*keywords):
    'Return relevant URIs ordered by relevance to the keyword(s)'
    keywords = normalize(keywords)
    marks = ', '.join('?' * len(keywords))
    query = search_query_template % marks
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute(query, keywords)
        rows = c.fetchall()
        return [uri for (uri,) in rows]

def parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser(description='keyword-searchable docuent database')
    parser.add_argument('database', help='name of the database file')
    parser.add_argument('--insert', '-i', type=argparse.FileType('r'),
                        help='filepath of doc')
    parser.add_argument('--search', '-s', nargs='+', dest='keywords',
                        help='space sepearated keywords')
    return parser.parse_args(*args, **kwargs)

if __name__ == '__main__':
    args = parse_args()
    database = args.database

    if args.insert:
        text = args.insert.read()
        uri = args.insert.name
        add_document(uri, text)

    if args.keywords:
        print '/n'.join(search(*args.keywords))


    
    
    
    

"""
Tests for docfinder.py
"""

from docfinder import *
from docfinder import create_db, normalize, score_document
import pprint, os

docdir = 'notes/peps'


if 0:
    print list(normalize(['Hettinger', 'enumerates', 'AND']))

if 0:
    filename = 'pep-0238.txt'
    fullname = os.path.join(docdir, filename)
    with open(fullname) as f:
        text = f.read()
    for term, score in score_document(text, n=10):
        print term, score

if 0:
    create_db(force=True)

if 0:
    #for filename in ['pep-0237.txt', 'pep-0236.txt', 'pep-0235.txt']:
    for filename in os.listdir(docdir):
        fullname = os.path.join(docdir, filename)
        with open(fullname, 'rb') as f:
            text = f.read()
        uri = os.path.splitext(filename)[0]
        print uri, len(text)
        add_document(uri, text)

if 0:
    print get_document('pep-0237')[:100]

if 1:
    #pprint.pprint(search('zip')[:10])
    pprint.pprint(search('zip', 'barry')[:10])


"""
$ sqlite3 pepsearch.db
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> .tables
Documents  Topics
sqlite> .schema Documents
CREATE TABLE Documents (uri text, document blob);
CREATE UNIQUE INDEX UriIndex ON Documents (uri);
sqlite> .schema Topics
CREATE TABLE Topics (term text, uri text, score real);
CREATE INDEX TermIndex ON Topics (term);
sqlite>
"""
        
        

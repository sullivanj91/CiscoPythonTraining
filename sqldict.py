'''
a dict-like, backed by a sqlite database.

- persistence
- concurrency
- introspectable
- sharable
'''

from collections import MutableMapping
import sqlite3

##Record = namedtuple('Record', 'key value')
##r = Record('key', 'value')
##r.key
##r.value

class SqlDict(MutableMapping):
    'dict-like, backed by a SQL database'

    def __init__(self, dbname, *args, **kwargs):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)

        c = self.connection.cursor()
        try:
            c.execute('CREATE TABLE Dict (key text, value text)')
            c.execute('CREATE UNIQUE INDEX key_index ON Dict (key)')
        except sqlite3.OperationalError:
            pass #ignore table already exists
        self.update(*args, **kwargs)
        

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        c = self.connection.cursor()
        c.execute('DELETE FROM Dict WHERE key=?', (key,))
        self.connection.commit()

    def __setitem__(self, key, value):
        if key in self:     # race condition
            del self[key]   # TODO: solve with better SQL
        c = self.connection.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))
        self.connection.commit()

    def __getitem__(self, key):
        c = self.connection.cursor()
        c.execute('SELECT value FROM Dict WHERE key=?', (key,))
        row = c.fetchone()
        if row is None:
            raise KeyError(key)
        return row[0]

    def __len__(self):
        c = self.connection.cursor()
        c.execute('SELECT count(key) FROM Dict')
        row = c.fetchone()
        return row[0]

    def __iter__(self):
        c = self.connection.cursor()
        c.execute('SELECT key FROM Dict')
        rows = c.fetchall()
        return iter([key for (key,) in rows])

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.dbname,self.items())

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, etype, einstance, etraceback):
        self.close()

        


if __name__ == '__main__':
    d = SqlDict('starwars.db')
    d['hero'] = 'Luke'
    d['villian'] = 'Darth'
    print d

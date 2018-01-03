#!/usr/bin/python2
import time
import sys
import rethinkdb as r
def create_tables(conn):
    tables = ['scores',
              'players',
              'challenges',
              ]
    for table in tables:
        r.db('acsc').table_create(table).run(conn)




def main():
    fail = time.time() + 30
    conn = None
    while conn is None:
        try:
            conn = r.connect('localhost')
        except:
            if time.time() > fail:
                print 'Got tired of waiting. Exiting'
                sys.exit(1)
            print 'Pausing for rethink to come up'
            time.sleep(1)
    r.db_create('acsc').run(conn)
    create_tables(conn)

    #TODO: This is a hack move it elsewhere
    while True:
        time.sleep(10)
if __name__ == '__main__':
    main()

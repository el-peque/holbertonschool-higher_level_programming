#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa """
import MySQLdb
import sys
from model_state import Base, State
import SQLAlchemy


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    if (len(query_rows) > 0):
        for row in query_rows:
            print(f"{row[0]}: {row[1]}")
    cur.close()
    db.close()

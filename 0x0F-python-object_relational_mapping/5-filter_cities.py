#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa """
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states, cities WHERE \
    cities.state_id = states.id AND states.name = %s ORDER BY \
    cities.id ASC", ((sys.argv[4],)))
    query_rows = cur.fetchall()

    if (len(query_rows) > 0):
        for i in range(0, len(query_rows) - 1):
            print(f"{query_rows[i][0]}", end=', ')
        print(query_rows[i + 1][0])
    cur.close()
    db.close()

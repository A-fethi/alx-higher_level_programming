#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               user=sys.argv[1],
                               port=3306,
                               password=sys.argv[2],
                               database=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM states, cities \
                WHERE cities.state_id=states.id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    database.close()

#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

database = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           port=3306,
                           password=sys.argv[2],
                           database=sys.argv[3])
cur = database.cursor()
cur.execute("SELECT * FROM states")
for row in cur.fetchall():
    print(row)
cur.close()
database.close()

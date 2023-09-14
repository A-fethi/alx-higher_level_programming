#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

database = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           port=3306,
                           password=sys.argv[2],
                           database=sys.argv[3])
cur = database.cursor()
state_name = sys.argv[4]
cur.execute("SELECT * FROM states WHERE NAME = %s", (state_name,))
for row in cur.fetchall():
    print(row)
cur.close()
database.close()
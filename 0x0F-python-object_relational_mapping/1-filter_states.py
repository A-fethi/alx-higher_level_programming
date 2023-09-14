#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

database = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           port=3306,
                           password=sys.argv[2],
                           database=sys.argv[3])
cur = database.cursor()
cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%'")
for row in cur.fetchall():
    print(row)
cur.close()
database.close()

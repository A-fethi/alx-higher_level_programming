#!/usr/bin/python3
""""takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               user=sys.argv[1],
                               port=3306,
                               password=sys.argv[2],
                               database=sys.argv[3])
    cur = database.cursor()
    state_name = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities, states \
                WHERE cities.state_id = states.id \
                AND states.name=%s", (state_name,))
    i = [row[0] for row in cur.fetchall()]
    print(", ".join(i))
    cur.close()
    database.close()

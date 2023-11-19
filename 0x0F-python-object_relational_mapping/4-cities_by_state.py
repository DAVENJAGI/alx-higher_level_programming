#!/usr/bin/python3
"""
Lists all cities from database hbtni_0e_o_usa
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(" SELECT cities.id, cities.name, state.name
                FROM cities INNER JOIN states
                ON cities.state_id=state.id ORDER BY cities.id")

    rows = cur.fetchall()

    for record in rows:
        print(record)

    cur.close()
    db.close()

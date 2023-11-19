#!/usr/bin/python3
"""
Lists all states from database hbtni_0e_o_usa
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         state_name=sys.argv[4], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%?%'
                ORDER BY id ASC", state_name)

    rows = cur.fetchall()

    for record in rows:
        print(record)

    cur.close()
    db.close()

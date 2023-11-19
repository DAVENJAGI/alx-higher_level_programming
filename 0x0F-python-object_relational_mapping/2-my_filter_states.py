#!/usr/bin/python3
"""
script that Lists all states from database hbtni_0e_o_usa table states
where name matches argument Results must be sorted in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()

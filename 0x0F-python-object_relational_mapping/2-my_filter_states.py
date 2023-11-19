#!/usr/bin/python3

"""
script that Lists all states from database hbtni_0e_o_usa table states
where name matches argument Results must be sorted in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbm = db.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3])
    cur = dbm.cursor()

    dbm.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows = dbm.fetchall()

    for row in rows:
        print(row)

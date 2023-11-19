#!/usr/bin/python3
"""
Script to list states name starting with
N (upper N) from database btn_0e_0_usa table states.
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' \
                    ORDER BY states.id ASC")

    rows = cur.fetchall()

    for record in rows:
        print(record)

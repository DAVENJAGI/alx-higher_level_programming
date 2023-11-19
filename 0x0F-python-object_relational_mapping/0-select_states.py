#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    res = cursor.fetchall()

    for rows in res:
        print(rows)

    cursor.close()
    db.close()

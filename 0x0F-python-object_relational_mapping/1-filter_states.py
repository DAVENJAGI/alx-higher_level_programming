#!/usr/bin/python3
"""
Script to list all states with name starting with uppercase N
from database.
"""

from MySQLdb import mysql
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDERD BY id ASC")
    rows = cur.fetchall()
    for record in rows:
        print(record)
    cur.close()
    db.close()

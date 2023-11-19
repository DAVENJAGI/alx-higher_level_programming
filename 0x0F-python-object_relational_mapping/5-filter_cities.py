#!/usr/bin/python3
"""
Lists all states from database hbtni_0e_o_usa
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM 'cities' as 'c' \
                INNER JOIN 'states' as 's' \
                ON 'c'.'state_id' = 's'.'id' \
                ORDER BY 'c'.'id'")

    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))

    cur.close()
    db.close()

#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="hbtn_0e_0_usa")

curcor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")

res = cursor.fetchall()

cursor.close()
db.close()

for row in res:
	print(row)

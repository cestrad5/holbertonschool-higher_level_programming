#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""

from sys import argv
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306,
                       user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
# Close all cursors
cur.close()
# Close all databases
conn.close()

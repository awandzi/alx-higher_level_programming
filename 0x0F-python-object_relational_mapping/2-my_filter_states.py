#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table"""
import MySQLdb
import sys
if ___name___ == "___main___":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        password=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.excute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = fetchall()
    for  row in rows:
        print(row)
    c.close()
    db.close()

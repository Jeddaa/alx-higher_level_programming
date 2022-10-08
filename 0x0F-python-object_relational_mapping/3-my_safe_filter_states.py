#!/usr/bin/python3
"""a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

connet = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
cursor = connet.cursor()
query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
cursor.execute(query, (argv[4],))
records = cursor.fetchall()
for i in records:
    print(i)
cursor.close()
connet.close()

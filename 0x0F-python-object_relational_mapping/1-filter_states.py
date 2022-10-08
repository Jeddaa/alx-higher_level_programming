#!/usr/bin/python3
"""a script that lists all states with name
starting with N from database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

connet = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
#create cursor to execute queries in SQL

cursor = connet.cursor()
query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
cursor.execute(query)
records = cursor.fetchall()
for i in records:
    print(i)
cursor.close()
connet.close()

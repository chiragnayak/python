print('-' * 75)

'''
postgreSQL - psycopg2 => pip install psycopg2
mysql - pymysql => pip install pymysql
'''

import psycopg2 as db
import sys
import sqlite3 as sql_db
import csv

# Establish the database connection
try:
    # conn = sql_db.connect('emp.db')
    conn = db.connect(host='localhost',
                      port=5432,
                      user='postgres',
                      password='train4sp',
                      database='vmware_db')

    cursor = conn.cursor()
except Exception as e:
    print(f'Error Occurred - {e.__class__.__name__}: {e}')
    print('-' * 75)
    sys.exit()
else:
    print('Database Connection Established')

print('-' * 75)

# Insert a record to emp_details
sql = """INSERT INTO emp_details(name, team, loc, sal) 
         VALUES('davies', 'testing', 'bangalore', 5000)"""
cursor.execute(sql)
conn.commit()
print('# of Records Inserted -', cursor.rowcount)

print('-' * 75)

# Read the data from csv file
with open(r'files\data.csv') as csv_read:
    all_recs = [tuple(rec[1:]) for rec in csv.reader(csv_read)]

# Insert multiple records to emp_details
sql = """INSERT INTO emp_details(name, loc, sal, team) 
         VALUES(%s, %s, %s, %s)"""
cursor.executemany(sql, all_recs[1:])
conn.commit()
print('# of Records Inserted -', cursor.rowcount)

print('-' * 75)

# Read the data from the table - fetchone
sql = "SELECT emp_id, name, loc, sal, team FROM emp_details"
cursor.execute(sql)

while True:
    rec = cursor.fetchone()
    if not rec:
        break
    print('Record -', rec)

print('-' * 75)

# Read the data from the table - fetchmany
sql = "SELECT emp_id, name, loc, sal, team FROM emp_details"
cursor.execute(sql)

while True:
    recs = cursor.fetchmany(5)
    if not recs:
        break
    print('Record -', recs)

print('-' * 75)

# Read the data from the table - fetchall
sql = "SELECT emp_id, name, loc, sal, team FROM emp_details"
cursor.execute(sql)
print('All Records -', cursor.fetchall())

print('-' * 75)

# Closing the database connection
cursor.close()
conn.close()
print('Database Connection Closed')

print('-' * 75)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
print("-" * 75)
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

print("-" * 75)

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()

mycursor.execute("SELECT * FROM customers")
print(mycursor.fetchall())

print("-" * 75)

# myresult = mycursor.fetchmany(5)
# myresult = mycursor.fetchone()

mycursor.execute("SELECT * FROM customers")
for x in mycursor:
    print(x)

print("-" * 75)


def func():
    return total + 1


total = 0

print(func())
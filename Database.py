import sqlite3
conn = sqlite3.connect('example.db')
print("Opened Database Successfully")

#Creating a Table
conn.execute(''' CREATE TABLE COMPLANY1(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL
);''')

print("Table Created Successfully")
conn.close()
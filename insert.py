import sqlite3
conn = sqlite3.connect('example.db')
print("Opened Database Successfully")

conn.execute("INSERT INTO COMPLANY1(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(1, 'EMOBILIS', 7, 'WESTLANDS', 25000.00)");

conn.execute("INSERT INTO COMPLANY1(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(2, 'Safaricom', 7, 'CBD', 35000.00)");

conn.execute("INSERT INTO COMPLANY1(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(3, 'Oracle', 7, 'Kilimani', 30000.00)");

conn.execute("INSERT INTO COMPLANY1(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(4, 'Microsoft', 7, 'Hurlingam', 55000.00)");

conn.commit()
print("Record Added Successfully")
conn.close()

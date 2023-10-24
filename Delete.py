import sqlite3
conn = sqlite3.connect('example.db')
print("Opened Database Successfully!")

conn.execute("DELETE FROM COMPLANY1 WHERE ID = 2")
conn.commit()

curser = conn.execute("SELECT id, name, age, address, salary FROM COMPLANY1")

for row in curser:
    print("ID =" [0])
    print("NAME =" [1])
    print("AGE =" [2])
    print("ADDRESS =" [3])
    print("SALARY =" [4])
print("Record Deleted Successfully!")
conn.close()
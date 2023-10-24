import sqlite3
conn = sqlite3.connect('example.db')
print("Opened Database Successfully!")


curser = conn.execute("SELECT id, name, age, address, salary from complany1")

for row in curser:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("ADDRESS =", row[3])
    print("SALARY =", row[4])

print("Operation Completed Successfully")
conn.close()

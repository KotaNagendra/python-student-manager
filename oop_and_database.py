class StudentRecord:
  def __init__(self, name, score):
    self.name=name
    self.score=score

  def check_status(self):
    if self.score>=50:
       return f"{self.name}: PASS"
    else:
       return f"{self.name}: FAIL"

student1=StudentRecord("Ananya", 78)
student2=StudentRecord("Rahul", 45)
student3=StudentRecord("Kiran", 92)

print(student1.check_status())
print(student2.check_status())
print(student3.check_status()) 

import sqlite3

connecton=sqlite3.connect("school.db")
cursor=connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
      name TEXT,
      score INTEGER
    )
""")

cursor.execute("INSERT INTO students (name,score) VALUES ('Ananya', 78)")
connection.commit()

cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()

print("Records inside the database:")
for row in rows:
  print(row)

connection.close()

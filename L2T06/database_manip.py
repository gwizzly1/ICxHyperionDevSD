'''
--------------------------------------
Task: Create a python file called database_manip.py. Write the code to do the following tasks:
- Create a table called python_programming
- Insert the following new rows into the python_programming table
- Select all records with a grade between 60 and 80
- Change Carl Davis's grade to 65
- Delete Dennie Fredrickson's row
- Change the grade of all people with an id below 55
--------------------------------------
'''

import sqlite3
db = sqlite3.connect('L2T06\python_programming')
cursor = db.cursor()


'''
---------- This is to create a table ------------
'''
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
''')
db.commit() # This causes it to bug out when the table already exists - therefore drop table at the end

'''
---------- This is to insert all values into the table ------------
'''

student_grades = [(55, 'Carl Davis', 61),(66, 'Dennis Fredrickson', 88), (77, 'Jane Richards', 78), (12, 'Peyton Sawyer', 45), (2, 'Lucas Brooke', 99)]
cursor.executemany(''' INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', student_grades)
db.commit()

'''
---------- This is to print all records with a grade between 60 and 80 ------------
'''
print('---------------------')
print("Filter for grades between 60 and 80:")
print('---------------------')
cursor.execute('''SELECT * FROM python_programming WHERE grade BETWEEN 60 and 80''')
for row in cursor:
    print(row)
    

'''
---------- This is to change Carl Davis's grade to 65 ------------
'''
grade = 65
name = 'Carl Davis'
cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ? ''', (grade, name))
db.commit()


print('---------------------')
print("Print out after changing Carl Davis's grade to 65:")
print('---------------------')
cursor.execute('''SELECT * FROM python_programming ''')
for row in cursor:
    print(row)

'''
---------- This is to delete Dennis Fredrickson's rows ------------
'''
id = 66
name = 'Dennis Fredrickson'
cursor.execute('''DELETE FROM python_programming WHERE id = ? AND name = ?''', (id, name))

db.commit()

print('---------------------')
print("Deleting Dennis Fredrickson's row:")
print('---------------------')
cursor.execute('''SELECT * FROM python_programming ''')
for row in cursor:
    print(row)


'''
---------- Change the grade of all people with an id below than 55----- 
----THIS QUESTION MAKES NO SENSE in the googledoc - The following is answering the question:-------
-------- 'Change the grade of all people with an id below 50 to 55'--------
'''
id = 50
grade = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < ? ''', (grade, id))
db.commit()

print('---------------------')
print("Change grade of all people with an id below 50 to 55:")
print('---------------------')
cursor.execute('''SELECT * FROM python_programming ''')
for row in cursor:
    print(row)




cursor.execute('''drop table python_programming''')
db.close()
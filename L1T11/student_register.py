'''
Aim: to produce a program that asks the user how many students they want to register, asks for the student id's and outputs a signiture line

Pseudocode:
Ask the number of students they wish to register
Ask for the ID for each individual student
Output the student IDs with '.........' appended after for the student's to sign.


Problem: I kept finding the '.' were being added as individual strings because I was using +=, not append, this was fixed after used append.
'''

register = input("Please submit how many student are registering:")
id_list = []

# For each number of students, enter the student ID and append '....' to the student ID
for student_num in range(int(register)):
    id_input = input("Please enter the student ID: ")
    id_list.append(id_input + '............')

print(id_list)

# This creates a new .txt file and adds the outputs
with open('output.txt', 'w') as f:
     f.write("\n".join(id_list))
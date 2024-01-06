'''
Task: Write a program that reads data from DOB.txt and prints it out in 2 different sections (name and DOB)
Plan:
1) Read the file and have a list of entire lines 
2) Iterate through the lines and save the 1st 2 words as name in another list
3) Iterate through the lines and save the last 3 words as birthdays in another list
4) Print these lists 
'''

# Read the contents from DOB.txt and split the lines into lists at the line breaks
with open('DOB.txt', '+r') as f:
    contents = f.read()

    line_list = contents.splitlines() # This splits the string into a list, seperating at the spaces

# Create empty lists called name_list and dob_list
name_list = []
dob_list = []

# For each line in the DOB.txt file, split into 3 sections: firstname, lastname and then the rest (ie dob)
# Append firstname and lastname to be full nane and then for each full name and dob, append them to the empty lists created above
for line in line_list:
    firstname, lastname, dob = line.split(' ', 2)
    name = firstname + ' ' + lastname
    name_list.append(name)
    dob_list.append(dob)

# This joins all strings in each list with a new line between them
name_list_3d = '\n'.join(name_list)
dob_list_3d = '\n'.join(dob_list)

print('Names')
print(name_list_3d)

print('DOB')
print(dob_list_3d)







'''
Pseudocode
1. Request user to input name and save as variable
2. Request user to input age and save as variable
3. Request user to input house_num and save as variable
4. Request user to input street_name and save as variable
5. Use f string to print sentence including all of the above
'''

name = input("Please enter your name: ")
age = input ("Please enter your age: ")
house_num = input("Please enter your house number: ")
street_name = input("Please enter your street name: ")

print(f"This is {name}. She is {age} years old and lives at house number {house_num} on {street_name}.")
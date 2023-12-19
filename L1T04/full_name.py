'''
Pseudocode:
1. Ask user to input their full name and store
2. Provide validation criteria and check against it
3. If the validations fail, print a statement to explain why 

'''

name = input("Please enter your full name:")

if name =="":
    print("Please enter a name")
elif len(name)>25:
    print("Your name is too long, are you sure it's only your name?")
elif len(name)<4:
    print("Your name is too short, please enter your full name.")
else:
    print("Thank you for submitting your name!")

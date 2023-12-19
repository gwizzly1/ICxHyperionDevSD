# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Name error - add quotation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # Logical Error - need this to be an f string (and swapped number_of_teeth and animal_type so it makes sense)

print (full_spec) # Syntax error - add brackets
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # This needed brackets (SyntaxError)
print ("\n") # Indented too much and needs brackets 

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" # Indented too much and change == to = to define a variable (syntaxError) and remove "years old" + formatted 'Str'
age = int(age_str) # Indented too much - have removed use below 
print ("I'm " + age_str + " years old.") # Indented too much and need to add spaces in + changed input to age_str

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # Indented too much and take away "" to keep the value as a integer (TypeError) + added the .5 to make it 3 years and 6 months
total_years = age + years_from_now 
answer_years = str(total_years)

print ("The total number of years: " + answer_years) # Need to remove the quotation marks (and change name) on "answer_years" for it to be a variable name and add a space

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = str(total_years * 12) # name error - changes to total_years and converted to str for the print statement below

print ("In 3 years and 6 months, I'll be " + total_months + " months old") # Add brackets and typeerror - can't print int + str so need to convert

#HINT, 330 months is the correct answer


#-----------------------------------------------
# Alternatively you could cut all the code down into:

print ("Welcome to the error program") # This needed brackets (SyntaxError)
print ("\n") # Indented too much and needs brackets 

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = 24 
print ("I'm " + str(age_str) + " years old.") 

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 
answer_years = str(age + years_from_now)

print ("The total number of years: " + answer_years) 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = str(total_years * 12) 

print ("In 3 years and 6 months, I'll be " + total_months + " months old") 

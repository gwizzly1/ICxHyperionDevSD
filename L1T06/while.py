"""
Looking to create a programme here where you can keep adding numbers (until user puts in -1) 
And then the program will return the mean of the numbers 

Pseudocode:

Set counter to 0, set sum_value to 0 and set choice to 0
Ask user to input a number
Whilst choice is not -1 change the choice variable to that value
Add that value to sum_value
Add 1 onto the counter
Loop this again and again until the value -1 is entered 
Calculate the average as sum_value/counter

"""
counter = 0
sum_value = 0
choice = 0


while True:
    choice = int(input("Please enter a number:"))

    if choice == -1:
        if counter == 0:
            raise ValueError("Average cannot be calculated: No values entered.")
        break
    
    sum_value += choice
    counter += 1
    


print(sum_value / counter)






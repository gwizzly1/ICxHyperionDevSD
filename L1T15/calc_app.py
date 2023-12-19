'''
Task: to create a calculation app that does simple calculations, stores them in a text file and can recall them
The app must only accept 2 numbers and an operation (+,-,*,/) as inputs
The app must be very robust and use defensive programming
If the user chooses to print previous equations, the programme must not crash if there is no text file
'''
import re # This allows me to always split from before/after the operator (eliminates the risk of incorrect number of spaces/ in the wrong place)

# create a function for the calculation
def calculation(num_1, operand, num_2):
    if operand == '+':
        return num_1 + num_2
    elif operand == '-':
        return num_1 - num_2
    elif operand == '*':
        return num_1 * num_2
    elif operand == '/':
        return num_1 / num_2
    else:
        print('This is not a valid calculation, please restart') # This stops different operands from being used - could also restart loop when this occurs


for attempts in range (8):
    initial_question = input('Would you like to view past calculations or calculate a new one? Please type \'new\' or \'previous\': ')

    if initial_question == 'previous': # this is to remove any blank spaces in the input
        try:
            with open('equations.txt', 'r+') as prev_file:
                prev_equations = prev_file.read()
                print(prev_equations) 
        except FileNotFoundError:
            with open('equations.txt', 'w') as new_file: # really not sure if this is the best way to open a blank file, I couldn't find a way to do it in one go
                print('File does not exist, empty file created')
            

    elif initial_question =='new': # this is to remove any blank spaces in the input
        for tries in range(5):
            for tries in range (5): # This is to ensure people only input 1 operator
                new_question = input('Please enter the calculation you want to do (number [space] operator (+-*/) [space] number):')
                qstn_char = len(new_question)
                qstn_char_rem = len(re.sub('\*|\/|\+|\-', '', new_question))
                spec_char= qstn_char - qstn_char_rem
                if(spec_char != 1):
                    print('Wrong number of operators, you need 1. Please restart')
                    
                else:
                    break
                

            try:
            # need to split up and save input into different components to calculate the result
            # firstly the below splits the input into 2 sections - before the special character and after the special character
            # then the 2 splits are converted to floats and saved as named variables (num_1 and num_2)
                split_num = re.split('\*|\/|\+|\-', new_question) # Have to use '\' before the special characters so regex can read it properly.
                num_1 = float(split_num[0]) # The white spaces included in these splits are removed when cast as a floats so no need to remove them
                num_2 = float(split_num[1])
            except (ValueError, NameError):
                print('This is not a valid input.')
        

            if ('+' in new_question):
                operand = '+'
                break
            elif('-' in new_question):
                operand = '-'
                break
            elif('*' in new_question):
                operand = '*'
                break
            elif('/' in new_question):
                operand = '/'
                break
            else:
                print('This is not a valid operand, please restart')

        try:
            result = calculation(num_1, operand, num_2)

            new_result = (f"{num_1}{operand}{num_2} = {result}")
            print(new_result)  
            with open('equations.txt', 'a+') as f:
                f.write(new_result+ "\n")
        except ZeroDivisionError:
            print('You cannot divide by 0, please try again')
    else:
        print('This is not an option, please restart') 
else:
    print('Too many attempts have been made, please start again.')
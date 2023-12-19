'''
Pseudocode:
1. Ask the user to input a sentence (and store the sentence)
2. Print the length of this sentence 
3. Find the last letter in the sentence
4. Replace all occurrances of this letter with '@'
5. Print the last 3 letters of the sentence backwards
6. Print a 5 letter word which consists of the 1st 3 letters + the last 2 letters

'''


str_manip = input("Please enter a sentence:")

print(len(str_manip))

last_let = str_manip[-1::] # This finds the last letter in the sentence
print(last_let)

print(str_manip.replace(last_let, "@")) # This replaces the last letter with '@'

print(str_manip[:-4:-1]) # This prints the last 3 letters in the sentence backwards 

print(str_manip[:3] + str_manip[-2:]) # This print sentence up to (and excluding) position 3 + from 2 from the end 
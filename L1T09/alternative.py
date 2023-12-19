"""
Task: Create a program that eads a string and makes every other letter uppercase and alternate letters lowercase.

Pseudocode:
1) User input
2) For each element in the list, if even make the element upper case and add to empty list, if odd make lower case and add to empty list
3) Print list
"""

# Read a string and then make each alternative letter upper case

sentence = input("Please write something: ")
alt_sentence = ""

for element in range(len(sentence)):
    if element %2:
        alt_sentence = alt_sentence + sentence[element].upper()
    else:
        alt_sentence = alt_sentence + sentence[element].lower()

print (alt_sentence)


"""
Task 2: Create a program that reads a sentence and makes every other word uppercase and alternate words lowercase.

Pseudocode:
1) User input (above)
2) Split the sentence by spaces (ie seperate words)
3) For each word in the sentence, do the same as above
"""


split_sen = sentence.split()

new_sen = ""

for word in range(len(split_sen)):
    if word %2:
        new_sen = new_sen +split_sen[word].upper() + " "
    else:
        new_sen = new_sen +split_sen[word].lower() + " "



print(new_sen)



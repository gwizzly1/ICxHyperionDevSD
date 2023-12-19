'''
Pseudocode
1. Save the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog."
2. Replace all of the '!' with spaces
3. Print the new sentence 
4. Print sentence in uppercase 
5. Print sentence in uppercase backwards
'''

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."


sentence_corr = sentence.replace("!"," ") # This replaces ! with spaces

print(sentence_corr)

sentence_upper = sentence_corr.upper() # This makes it all uppercare

print(sentence_upper)

print (sentence_upper[::-1]) # This reverses the string and therefore prints it uppercase and backwards


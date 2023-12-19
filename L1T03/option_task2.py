'''
Pseudocode:
1. Ask users input of their favourite restaurant - store this
2. Ask users input of their favourite number - store this
3. Print the results of these things
4. Explain why you can't cast the text as a number
'''


string_fav = input("Please enter the name of your favourite restaurant:")
int_fav = int(input("Please enter your favourite number:"))

print(string_fav)
print(int_fav)

# print(int(string_fav))
# This doesn't work as it's text, you can't convert text to an integer


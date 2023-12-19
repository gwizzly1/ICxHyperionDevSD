"""
Recursion task:
Create a function that takes a list of integers and a single integer as arguments. The single integer will represent an index point.
The function needs to add the sum of all the numbers in the list up until and including the index point using recursion.

Pseudocode:
1) User input(one list of numbers and 1 integer)
2) Look up the index given in the list 
3) Add this value to the index-1 in the list
4) Call this recursive function at each (index-1) until it reaches index[0]
5) Print the sum of values
"""

def adding_up_to(list_input, index):
    if index == 0:
        return list_input[0]
    return list_input[index] + adding_up_to(list_input, index - 1)

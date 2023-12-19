"""
Recursion task 2:
Create a function that returns the largest number in a list of integers taken in as arguments.

Pseudocode:
1) User input (list of numbers) 
2) Base Case = when you're at the last value in the list return that value
3) Starting from the end of the list compare the last value to the function of values (- the last one)
4) When base case is hit print that value as it'll be the max
"""

def largest_number(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list.pop()
    return max(numbers_list.pop(), largest_number(numbers_list)) 
    
'''
Pseudocode:
1. Ask the user to input the lengths of the 3 sides of a triangle
2. Save variable s as (side 1 + side 2 + side 3)/2
3. Use the above to work out the area of the triangle using the equation listed
4. Print area
'''

import math

length1 = input("Please write length of side 1 of a triangle:")
length2 = input("Please write length of side 2 of a triangle:")
length3 = input("Please write length of side 3 of a triangle:")

s = (int(length1)* int(length2) * int(length3))/2

area = math.sqrt(s*(s-int(length1))*(s-int(length2))*(s-int(length3)))

print(area)
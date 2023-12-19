"""
Create a single loop + if/else condition that creates the following pattern:
*
**
***
****
*****
****
***
**
*

Pseudocode:
for values between 1 and 9
if the value is 5 or below print the number of * equal to the value
if the value is above 5: (i-5)/2 is the difference between expected and i
i-this gives us the number of * we want. Then we x '*' to get the picture we expect
"""

for i in range(1,10):
    if i<6:
        print(i * '*')
    else:
        print ((i-((i-5)*2))*'*')


''' Task: Deciding what award a triathlete receives. 

Pseudocode:
1. Read times for running, swimming and cycling
2. Add up the times for total time racing
3. If total time is less than 100 minutes (within qualifying time) then they are awarded provincial colours
4. If total time is within 105 minutes (5 minutes over qualifying time) they are awarded half provincial colours
5. If total time is within 110 minutes (10 mins over qualifying time) they are awarded provincial scroll
6. After this they get no award
'''

# Could ask the user to input the times (below) 
time_running = float(input('Please enter the time you ran in (in minutes):'))
time_swimming = float(input('Please enter the time you swam in (in minutes):'))
time_cycling = float(input('Please enter the time you cycled in (in minutes):'))


total = time_running + time_swimming + time_cycling

print(f'Total = {total}')

if total < 100: # this is not <= as the time has to be less than 100 (100 minutes is over qualifying time)
    print("You won PROVINCIAL COLOURS!")
elif total < 100 + 5:
    print("You won HALF PROVINCIAL COLOURS")
elif total < 100 + 10:
    print("You won the PROVINCIAL SCROLL")
else:
    print("I'm sorry, no prizes were won this time")

"""
In my feedback it says it doesn't produce the correct results but the way I'm reading the question is that if the total time is within 100 mins + 5 they get 1/2 colours 
and if it's within 100 minutes + 10 they get the scroll, is that wrong? 
I say that because surely it doesn't make sense the other way around: why when you end up with a faster time would you suddenly get 1/2 colours instead of full colours?
"""
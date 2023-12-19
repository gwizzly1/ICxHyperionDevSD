'''
This task is to calculate the costs of various holiday options (plane, hotel and car rental). 

Pseudocode:
1) get input for location (paste 'this is not an option, please input again' if they're not in the list)
2) get input for number of nights in a hotel
3) get input for number of hire car days 
4) create dictionaries for location: hotel price per night, location: flight cost,location: car rental cost
5) create functions:
    hotel_cost => is location is x then hotel cost = location lookup price* number of nights(input)
    plane_cost => if location is x then plane cost = location lookup in cost dictionary
    car_cost => if location is x then car cost = locaiton lookup. cost* number of nights(input)
6) add up total of the holiday cost
7) print in pretty format
'''

flt_cost_dict = {'LDN':150, 'DOH':570, 'ITA': 350}
hotel_cost_dict = {'LDN': 300, 'DOH': 100, 'ITA': 250}
car_cost_dict = {'LDN': 40, 'DOH': 75, 'ITA': 50}


def flight_cost(loc_input):
    """This looks up the chosen location in the dictionary of flight costs"""
    return flt_cost_dict[loc_input]


def hotel_cost(loc_input, hotel_nights_input):
    """This looks up chosen location in dictionary of daily hotel costs and multiplies it by the number of days input"""
    return float(hotel_cost_dict[loc_input]) * float(hotel_nights_input)


def car_hire_cost(loc_input, car_days_input):
    """This looks up chosen location in dictionary of daily car hire costs and multiplies it by the number of days input"""
    return float(car_cost_dict[loc_input])* float(car_days_input)


def holiday_cost(loc_input, hotel_nights_input, car_days_input):
    """This adds up all of the previous costs to result in the total holiday cost"""
    total_holiday_cost_1 = flight_cost(loc_input)+ hotel_cost(loc_input, hotel_nights_input) + car_hire_cost(loc_input, car_days_input)
    return(total_holiday_cost_1)


def main():
    for attempts in range(5): # This is to make sure the user chooses a valid country code
        loc_input = input('Please input your destination of choice from: LDN, DOH, ITA:').upper()
        if loc_input not in ('LDN', 'DOH', 'ITA'):
            print('This is not a supported location, please try again.')
        else:
            break

    for attempts in range(5): # This is to make sure the user chooses a valid number
        hotel_nights_input = input('Please input the number of nights you will stay at a hotel:').strip() # To remove leading/trailing spaces
        if not hotel_nights_input.isnumeric(): # LEARNING: bool(re.search('[a-zA-Z]', hotel_nights_input)) == True - previously used this but 1) no need for ==True (as if already assumes if true and 2) this ignores symbols. isnumeric allows it only to be numeric
            print('This only accepts numbers, please try again.')
        else:
            break

    for attempts in range(5):
        car_days_input = input('Please input the number of days you need to hire a car:').strip() 
        if not car_days_input.isnumeric(): 
            print('This only accepts numbers, please try again.')
        else:
            break

    total_flight_cost = flight_cost(loc_input)
    total_hotel_cost = hotel_cost(loc_input, hotel_nights_input)
    total_car_hire_cost = car_hire_cost(loc_input, car_days_input)
    total_holiday_cost = holiday_cost(loc_input, hotel_nights_input, car_days_input)


    print('Flight cost: ')
    print(total_flight_cost)
    print('Hotel cost:')
    print(total_hotel_cost)
    print('Car hire cost:')
    print(total_car_hire_cost)
    print('Total holiday cost')
    print(total_holiday_cost)


if __name__ == '__main__':
    main()

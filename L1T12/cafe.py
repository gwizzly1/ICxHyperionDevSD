'''
Task: to create a list of stock items, a dictonary of these stock items alongside their stock levels and the price 
then to calculate the total inventory value by looping through the dictionary

Pseudocode:
1) Create list of stock items, []
2) Create a dictionary - stock item: stock amount {}
- how to make it more efficient (don't need to update all 3 lists each time something gets added?)
3)  Create a disctionary of prices - stock item: price {}
4) Calculate total-stock-worth by looping through both the stock amount and prices for each item and printing name & price*amount
 - will need to += at each stage for total 
'''

stock_items_lst = ['bread','butter','milk','eggs','ham']

items_amount_dict = {'bread':3,'butter':6,'milk':2,'eggs':8,'ham':1}

items_prices_dict = {'bread':1.50,'butter':3.00,'milk':1.50,'eggs':4.00,'ham':4.50}

total_value_dict = {}


# For each item in the stock list this prints the name, a lookup to the items_amount_dict and a lookup to the items_prices_dict, 
#   at the end it multiplies these values together to result in the total value of the item in stock and adds this to a total_value_dictionary
for items in stock_items_lst:
    print(items, items_amount_dict[items], items_prices_dict[items],(items_amount_dict[items]* items_prices_dict[items]))
    total_value_dict[items] = items_amount_dict[items]* items_prices_dict[items]


print('Total stock value: ')
print(sum(total_value_dict.values()))
    
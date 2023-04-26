"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock

# YOUR CODE STARTS HERE


def order_function():
    # It asks the user if he wants to order the particular item and if yes how many of them
    order = input('Would you like to order this item?(y/n)')
    if order == 'n':                        # if no, don't do anything
        pass
    if order == 'y':
        amount = int(input('How many would you like?'))     # if yes, ask how many?
        if amount < w1 + w2 or amount == w1 + w2:
            print(f'{amount} {i_name} have been ordered.')    # if ordered amount is less than available
        else:
            print(f'There are not this many available. The maximum amount that can be ordered is {w1 + w2}')
            order_function()                               # calls itself if more than available to ask for less
    else:
        pass


def action_1(item):
    # List items in both warehouses with names from which they are: 1 or 2
    # print the total amount of items in stock on each warehouse
    w11 = 0
    w21 = 0
    for items in stock:
        if item == (items['state'] + ' ' + items['category']):
            if items['warehouse'] == 1:
                w11 = w11 + 1
            elif items['warehouse'] == 2:
                w21 = w21 + 1

    return [w11, w21]


from datetime import datetime


def calc_time(stored_date):
    stored_date = datetime.strptime(stored_date, '%Y-%m-%d %H:%M:%S')
    datetime_now = datetime.now()
    return (datetime_now - stored_date).days


def action_2(item_name, wh1, wh2):
    # search of the items (operation number `2`) so that:
    # 1. If the search returns at least one result (in any warehouse), it prints a list of all the items
    # showing the name of the warehouse and the number of days it has passed since they were stocked.
    # 2. It still prints the maximum availability only when the item is found in more than one warehouse.
    # 3. It still prints `Location: Not in stock` when the item is not found.

    if wh1 == 0 and wh2 == 0:
        print('Location: Not in stock')                          # if no such item exists in any of the warehouses
    elif wh2 > 0 or wh1 > 0:
        print(f'Amount available: {w1+w2}')
        for items in stock:
            if item_name == (items['state'] + ' ' + items['category']):
                print(f"Warehouse {items['warehouse']} (in stock for {calc_time(items['date_of_stock'])} days)")          # if item is available only in warehouse 1
        # order_function()                   # Function call to place order
        if wh2 > 0 and wh1 > 0:

            if wh1 > wh2:
                print(f'Maximum availability: {wh1} in Warehouse 1')  # if more no of items are available in warehouse 1
            elif wh1 < wh2:
                print(f'Maximum availability: {wh2} in Warehouse 2')  # if more no of items are available in warehouse 2
            else:
                print(f'Both warehouses have same availability: {wh1}')  # if same no of items are available in both
        order_function()                    # Function call to place order


def curate_name(item_name):
    # It produces the same result when typing `cheap tablet` and `CHEAP TABLET`
    # (the search should be ** case insensitive **).

    item_name = item_name.lower()
    if len(item_name.split()) == 2 or len(item_name.split()) == 1:
        item_name = item_name.title()
    else:
        x = item_name.split(" ")
        item_name = x[0].capitalize() + ' ' + x[1] + ' ' + x[2].capitalize()
    return item_name


def action_3():
    # 1. Show a menu of available categories. This menu will have to include a numeric code (the number the user will
    # type in to select a category), the name of the category and the amount of items available in that
    # category (in any warehouse).
    # 2. Ask the user to type the category number of their choice.
    # 3. List all items in that category. This time, print them one after the other (not separated by warehouse)
    # and include the name of the warehouse at the end of each line.

    new_list = {}
    temp_dict = {}
    for items in stock:
        if any(items['category'] in s for s in new_list):
            new_list[items['category']] = new_list[items['category']] + 1
        else:
            new_list[items['category']] = 1
    print(new_list)
    v = list(new_list.values())
    for number, letter in enumerate(new_list):
        temp_dict[number+1] = letter
        print(number+1, letter, v[number])
    b = int(input('Type the number of the category to browse:'))
    for items in stock:
        if items['category'] == temp_dict[b]:
            print(items['state'] + ' ' + items['category'], 'Warehouse:', items['warehouse'])


# ---------------------------------------------------------------------------------------------------------------------
# main function starts here
name = input('What is your name?')          # Get the username
name = curate_name(name)
print(f'Hallo, {name}!')                # Greet the user

# Show the menu and ask to pick a choice
print('What would you like to do? 1. List items by warehouse 2. Search an item and place an order 3. Browse by '
      'category 4. Quit')
action = (input('Type the number of the operation you want'))     # Accept user input from above list
if action == '1':
    i_name = input('Please input the item name')               # name of the item from user in main
    [w1, w2] = action_1(i_name)                                                      # if 1: call function
    print(f'Total items in warehouse 1: {w1}')
    print(f'Total items in warehouse 2: {w2}')

elif action == '2':
    i_name = input('Please input the item name')
    i_name = curate_name(i_name)
    print(f'What is the name of the item? {i_name}')
    [w1, w2] = action_1(i_name)
    action_2(i_name, w1, w2)                                            # if 2: call function

elif action == '3':
    action_3()


elif action == '4':
    pass                                                        # quit
else:
    print(f'{action} is not a valid operation. Please give input as: 1, 2 or 3')   # invalid input

print(f'\nThank you for your visit, {name}!')                 # Thank the user for the visit


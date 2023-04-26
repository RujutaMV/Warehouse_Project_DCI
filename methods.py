from datetime import datetime
from data import stock


def add_keys():
    warehouse1 = {}
    for items in stock:
        key = items['warehouse']
        if key in warehouse1.keys():
            pass
        else:
            warehouse1[key] = 0
    return warehouse1


def list_items_by_warehouse(item):
    # List items in both warehouses with names from which they are: 1 or 2
    # print the total amount of items in stock on each warehouse
    warehouse = {}
    flag = 0
    for items in stock:
        if item == (items['state'] + ' ' + items['category']):
            key = items['warehouse']
            if key in warehouse.keys():
                warehouse[key] = warehouse[key] + 1
            else:
                warehouse[key] = 1
            flag = 1
    if flag == 0:
        print('Item is not present')
        warehouse = add_keys()

    return warehouse

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


def calc_time(stored_date):
    stored_date = datetime.strptime(stored_date, '%Y-%m-%d %H:%M:%S')
    datetime_now = datetime.now()
    return (datetime_now - stored_date).days


def order_function(order_dict, i_name):
    # It asks the user if he wants to order the particular item and if yes how many of them
    order = input('Would you like to order this item?(y/n)')
    if order == 'n':                        # if no, don't do anything
        pass
    if order == 'y':
        amount = int(input('How many would you like?'))     # if yes, ask how many?
        if amount <= sum(order_dict.values()):
            print(f'{amount} {i_name} have been ordered.')    # if ordered amount is less than available
        else:
            print(f'There are not this many available. The maximum amount that can be ordered is {sum(order_dict.values())}')
            order_function(order_dict, i_name)                           # calls itself if more than available to ask for less
    else:
        pass

def search_and_order_item():
    # search of the items (operation number `2`) so that:
    # 1. If the search returns at least one result (in any warehouse), it prints a list of all the items
    # showing the name of the warehouse and the number of days it has passed since they were stocked.
    # 2. It still prints the maximum availability only when the item is found in more than one warehouse.
    # 3. It still prints `Location: Not in stock` when the item is not found.
    item_name = input('Please input the item name')
    # i_name = curate_name(i_name)
    print(f'What is the name of the item? {item_name}')
    w = list_items_by_warehouse(item_name)

    if all(value == 0 for value in w.values()):
        print('Location: Not in stock')                          # if no such item exists in any of the warehouses
    elif any(value != 0 for value in w.values()):
        print(f'Amount available: {sum(w.values())}')
        for items in stock:
            if item_name == (items['state'] + ' ' + items['category']):
                print(f"Warehouse {items['warehouse']} (in stock for {calc_time(items['date_of_stock'])} days)")          # if item is available only in warehouse 1
        if all(value != 0 for value in w.values()):
            v = list(w.values())
            k = list(w.keys())
            print(f'Maximum availability: {max(v)} in Warehouse{k[v.index(max(v))]}')

        order_function(w, item_name)                    # Function call to place order

def browse_by_category():
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
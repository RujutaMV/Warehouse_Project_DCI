"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE


def order_function():
    # It asks the user if he wants to order the particular item and if yes how many of them
    order = input('Would you like to order this item?(y/n) ')
    if order == 'n':                        # if no, don't do anything
        pass
    if order == 'y':
        amount = int(input('How many would you like?'))     # if yes, ask how many?
        if amount < w1 + w2 or amount == w1 + w2:
            print(f'{amount} {item_name} have been ordered.')    # if ordered amount is less than available
        else:
            print(f'There are not this many available. The maximum amount that can be ordered is {w1 + w2}')
            order_function()                               # calls itself if more than available to ask for less
    else:
        print('Invalid Input: Input (y/n)')
        order_function()                                    # calls itself asking to put correct input


def action_1():
    # List items in both warehouses with names from which they are: 1 or 2
    print('Items in Warehouse 1:')
    for items in warehouse1:
        print(items)                                        # print items in warehouse 1
    print('Items in Warehouse 2:')
    for items in warehouse2:
        print(items)                                        # print items in warehouse 2


def action_2(w1, w2):
    # Search an item and place an order : if available call order_function()
    print(f'The total amount of items in the warehouses are: {w1 + w2}')
    if w1 == 0 and w2 == 0:
        print('Not in stock')                          # if no such item exists in any of the warehouses
    elif w2 == 0:
        print('Location: Warehouse 1')          # if item is available only in warehouse 1
        order_function()                   # Function call to place order
    elif w1 == 0:
        print('Location: Warehouse 2')          # if item is available only in warehouse 2
        order_function()                    # Function call to place order
    else:
        print('Location: Both warehouses')          # if item is available only in both warehouses
        if w1 > w2:
            print(f'Maximum availability: {w1} in Warehouse 1')  # if more no of items are available in warehouse 1
        elif w1 < w2:
            print(f'Maximum availability: {w2} in Warehouse 2')  # if more no of items are available in warehouse 2
        else:
            print(f'Both warehouses have same availability: {w1}')  # if same no of items are available in both
        order_function()                    # Function call to place order


name = input('What is your name?')          # Get the username
print(f'Hallo, {name}!')                # Greet the user

# Show the menu and ask to pick a choice
print('What would you like to do? 1. List items by warehouse 2. Search an item and place an order 3. Quit')
action = (input('Type the number of the operation you want'))     # Accept user input from above list
if action == '1':
    action_1()                                                      # if 1: call function
elif action == '2':
    consent = 'y'                           # hardcode value to always enter loop once
    while consent == 'y':                    # loop to order multiple items, always enter the loop first time
        item_name = input('Please input the item name')
        w1 = warehouse1.count(item_name)                # no of items in warehouse 1
        w2 = warehouse2.count(item_name)                # no of items in warehouse 2
        action_2(w1, w2)                                            # if 2: call function
        consent = input('Would you like to order another item?(y/n) ')    # ask user if he wants to order more items
elif action == '3':
    pass                                                # quit
else:
    print(f'{action} is not a valid operation. Please give input as: 1, 2 or 3')   # invalid input

print(f'\nThank you for your visit, {name}!')                 # Thank the user for the visit


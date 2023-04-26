"""Command line interface to query the stock.
To iterate the source data you can use the following structure:
for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
from Warehouse_Project_DCI.methods import list_items_by_warehouse
from Warehouse_Project_DCI.methods import curate_name, search_and_order_item, browse_by_category

# main function starts here
name = input('What is your name?')          # Get the username
name = curate_name(name)
print(f'Hallo, {name}!')                # Greet the user
action = 1
while action != 4:
    # Show the menu and ask to pick a choice
    print('What would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Browse '
          'by category \n4. Quit')
    action = (input('Type the number of the operation you want'))     # Accept user input from above list
    if action == '1':
        i_name = input('Please input the item name')               # name of the item from user in main
        w = list_items_by_warehouse(i_name)                  # if 1: call function -List items by warehouse
        for i in w:
            print(f'Total items in warehouse {i}: {w[i]}')
    elif action == '2':
        search_and_order_item()
    elif action == '3':
        browse_by_category()
    elif action == '4':
        pass                                                        # quit
        break
    else:
        print("*" * 70)
        print(f'{action} is not a valid operation. Please give input as: 1, 2 ,3 or 4')   # invalid input
        print("*" * 70)

print(f'\nThank you for your visit, {name}!')                 # Thank the user for the visit

# ______________________________________________________________________________

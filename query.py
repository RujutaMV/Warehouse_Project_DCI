"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
# from methods import list_items_by_warehouse
from methods import greet_user


def main():                                  # main function starts here
    greet_user()


if __name__ == '__main__':
    main()


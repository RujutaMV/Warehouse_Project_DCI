from datetime import datetime


class Item:
    def __init__(self, state: str = None, category: str = None, warehouse: int = 1, date_of_stock: str = None):     # datetime format: "yyyy-mm-dd hh:mm:ss"
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock

    def __str__(self):
        item = self.state + ' ' + self.category
        return f"Item: {self.state} {self.category}"


class Warehouse:
    def __init__(self, w_id: int = None) -> None:
        self.id = w_id
        self.stock = []

    def occupancy(self) -> int:
        return len(self.stock)

    def add_item(self, new_item):
        self.stock.append(new_item)

    def search(self, search_item) -> list:
        new_list = []
        for items in self.stock:
            if search_item in (items.state + ' ' + items.category):
                new_list.append(items.state + ' ' + items.category)
        return new_list


class User:
    def __init__(self, user_name: str = "Anonymous", is_authenticated: bool = False):
        self._name = user_name

    def authenticate(self, password: str) -> False:
        return False

    def is_named(self, name: str) -> bool:
        if name == self._name:
            return True
        else:
            return False

    def greet(self) -> None:
        print(f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking "
              "for,\nplease ask one of our staff members to assist you.")

    def bye(self) -> None:
        print(f'\nThank you for your visit, {self._name}!')


class Employee(User):
    def __init__(self, user_name: str, password: str = None, head_of: list = []):
        User.__init__(self, user_name)
        self.__password = password
        self.head = head_of

    def authenticate(self, password: str) -> bool:
        if password == self.__password:
            return True
        else:
            return False

    def order(self, item, amount):
        print(f'Order placed for: {item} and amount: {amount}')

    def greet(self) -> None:
        print(f"Hello, {self._name}!\nIf you experience a problem with the system, please contact technical "
              "support.")

    def bye(self) -> None:
        print('Summary of Actions:')
        User.bye(self)

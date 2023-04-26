from unittest.mock import patch
from data import stock

# unittests
from start import curate, search_and_order_item, list_of_personnel, curate_mock
# from classes import User, Employee, Warehouse
import unittest


class TestClass(unittest.TestCase):
#
    def test_employee_with_choice1(self):
        person = curate('1', 'Jeremy')                # assert person is employee
        self.assertTrue(str(person.__class__) == "<class 'classes.Employee'>")

    def test_employee_with_choice1b(self):
        person = curate('1', 'Jeremy')
        self.assertFalse(str(person.__class__) == "<class 'classes.User'>")

    def test_user_with_choice1(self):
        self.assertIsNone(curate('1', 'Rujuta'))   # since 1,user pair is wrong returns None

    def test_user_with_choice2(self):
        person = curate('2', 'Rujuta')
        self.assertTrue(str(person.__class__) == "<class 'classes.User'>")

    def test_user_with_choice2b(self):
        person = curate('2', 'Rujuta')
        self.assertFalse(str(person.__class__) == "<class 'classes.Employee'>")

    def test_any_with_other_choice(self):
        self.assertIsNone(curate('4', 'Rujuta'))     # for any choice other than '1' or '2'

    @patch('start.curate')
    def test_any_with_other_choice_mock(self, mock_data):
        mock_data.return_value = 'User Class'
        self.assertIsNotNone(curate_mock('4', 'Rujuta'))     # for any choice other than '1' or '2'

    def test_personnel(self):
        self.assertIsInstance(list_of_personnel(), dict)

    def test_user_authenticate(self):
        person = curate('2', 'Rujuta')
        self.assertFalse(person.authenticate(password='Rujuta'))

    def test_employee_authenticate(self):
        person = curate('1', 'Jeremy')
        self.assertTrue(person.authenticate(password='coppers'))

    def test_employee_wrong_password(self):
        person = curate('1', 'Jeremy')
        self.assertFalse(person.authenticate(password='Jeremy'))


    # def test_user_cannot_order(self):
    #     person = curate('2', 'Rujuta')
    #     self.assertFalse(search_and_order_item(person))   # for user return false

    # def test_employee_can_order(self):
    #     person = curate('1', 'Jeremy')            # for employee return true
    #     self.assertTrue(search_and_order_item(person))     # password = coppers, Funny Smartphone: 3



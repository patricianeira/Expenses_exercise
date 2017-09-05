import unittest
from Expenses import Expenses
from contextlib import contextmanager
from StringIO import StringIO
import sys

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class ExpensesTest(unittest.TestCase):

    def test_not_option_add_expense(self):
        exp = Expenses()
        operation = 'Add'
        input_list = ['Add', '2', 'gy']
        with captured_output() as (out, err):
            exp.add_expense(operation, input_list)
        output = out.getvalue().strip()
        self.assertEqual(output, "Just 3 options: food, transportation, gym")

    def test_number_option_add_expense(self):
        exp = Expenses()
        operation = 'Add'
        input_list = ['Add', '2', '4']
        with captured_output() as (out, err):
            exp.add_expense(operation, input_list)
        output = out.getvalue().strip()
        self.assertEqual(output, "Just 3 options: food, transportation, gym")

    def test_number_is_string_add_expense(self):
        exp = Expenses()
        operation = 'Add'
        input_list = ['Add', 'E', 'gym']
        with captured_output() as (out, err):
            exp.add_expense(operation, input_list)
        output = out.getvalue().strip()
        self.assertEqual(output, "The 2nd parameter has to be a number")

    def test_empty_read_file(self):
        exp = Expenses()
        exp.read_file("test_empty.txt")
        self.assertEqual(exp.food, 0)
        self.assertEqual(exp.transport, 0)
        self.assertEqual(exp.gym, 0)


if __name__ == '__main__':
    unittest.main()
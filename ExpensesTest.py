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

    def test_equal_print_expenses(self):
        exp = Expenses()
        exp.concepts = ["food","transportation","gym"]
        exp.quantities = ["10","15","15"]
        with captured_output() as (out, err):
            exp.print_expenses(exp.concepts)
        output = out.getvalue().strip()
        self.assertEqual(output, "10 food\n15 transportation\n15 gym")

    def test_not_equal_print_expenses(self):
        exp = Expenses()
        exp.concepts = ["food","transportation","gym"]
        exp.quantities = ["10","15","15"]
        with captured_output() as (out, err):
            exp.print_expenses(exp.concepts)
        output = out.getvalue().strip()
        self.assertNotEqual(output, "10 food\n15 transportation\n20 gym")

    def test_equal_print_total(self):
        exp = Expenses()
        operation = "Added"
        quantity = "4"
        activity = "gym"
        total = "45"
        with captured_output() as (out, err):
            exp.print_total(operation, quantity, activity, total)
        output = out.getvalue().strip()
        self.assertEqual(output, "4 pesos Added to gym - Total: 45 pesos")

    def test_not_equal_print_total(self):
        exp = Expenses()
        operation = "Added"
        quantity = "4"
        activity = "gym"
        total = "45"
        with captured_output() as (out, err):
            exp.print_total(operation, quantity, activity, total)
        output = out.getvalue().strip()
        self.assertNotEqual(output, "4 pesos Added to gym - Total: 46 pesos")

    def test_wrong_option_process_input(self):
        exp = Expenses()
        user_input = "Hi"
        with captured_output() as (out, err):
            exp.process_input(user_input)
        output = out.getvalue().strip()
        self.assertEqual(output, "Not an option")

    def test_wrong_concept_add_expense(self):
        exp = Expenses()
        quantity = '6'
        concept = "g"
        with captured_output() as (out, err):
            exp.add_expense(quantity, concept)
        output = out.getvalue().strip()
        self.assertEqual(output, "The concept is incorrect")

    def test_not_digit_add_expense(self):
        exp = Expenses()
        quantity = 'r'
        concept = "gym"
        with captured_output() as (out, err):
            exp.add_expense(quantity, concept)
        output = out.getvalue().strip()
        self.assertEqual(output, "The 2nd parameter has to be a number")

    def test_read_file(self):
        exp = Expenses()
        exp.path_file = "test.txt"
        exp.read_expenses_file()
        self.assertNotEqual(len(exp.concepts),0)

    def test_empty_read_file(self):
        exp = Expenses()
        exp.path_file = "test_empty.txt"
        exp.read_expenses_file()
        with captured_output() as (out, err):
            exp.read_expenses_file()
        output = out.getvalue().strip()
        self.assertEqual(len(exp.concepts), 0)
        self.assertEqual(output, "The file is empty")

if __name__ == '__main__':
    unittest.main()
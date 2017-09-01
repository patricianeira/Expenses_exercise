import unittest
import Expenses
from Expenses import process_input

class ExpensesTest(unittest.TestCase):
    def test_process_input(self):
        exp = Expenses()
        exp.food = 10
        exp.transport = 12
        exp.gym = 13
        exp.data = "Add 5 food"
        self.assertTrue(process_input(exp))

if __name__ == '__main__':
    unittest.main()

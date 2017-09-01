import unittest
from Expenses import Expenses

class ExpensesTest(unittest.TestCase):
    def test_process_input(self):
        exp = Expenses()
        exp.food = 10
        exp.transport = 12
        exp.gym = 13
        exp.data = "Add 5 food"
        self.assertTrue(exp.process_input())

if __name__ == '__main__':
    unittest.main()

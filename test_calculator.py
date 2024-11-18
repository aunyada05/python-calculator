import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #--------------------------add
    def test_add(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add(self):
        self.assertEqual(self.calc.add(1, -2), -1)

    #--------------------------subtract
    def test_add(self):
        self.assertEqual(self.calc.subtract(-3, -1), -2)

    def test_add(self):
        self.assertEqual(self.calc.subtract(-3, 1), -4)

    #--------------------------multiply
    def test_add(self):
        self.assertEqual(self.calc.multiply(-1, -3), 3)

    def test_add(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)

    #--------------------------divide
    def test_add(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_add(self):
        self.assertEqual(self.calc.divide(-6, 2), -3)

    #--------------------------modulo
    def test_add(self):
        self.assertEqual(self.calc.modulo(4, 2), 0)

    def test_add(self):
        self.assertEqual(self.calc.modulo(4, 5), 4)
    

if __name__ == '__main__':
    unittest.main()
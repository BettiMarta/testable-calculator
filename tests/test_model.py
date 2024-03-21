import unittest
from calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_initial_expression_is_empty(self):
        self.assertEqual("", self.calculator.expression)

    def test_digit(self):
        self.calculator.digit(1)
        self.assertEqual("1", self.calculator.expression)

    def test_plus(self):
        self.calculator.plus()
        self.assertEqual("+", self.calculator.expression)

    def test_minus(self):
        self.calculator.minus()
        self.assertEqual("-", self.calculator.expression)
    
    def test_multiply(self):
        self.calculator.multiply()
        self.assertEqual("*", self.calculator.expression)
    
    def test_divide(self):
        self.calculator.divide()
        self.assertEqual("/", self.calculator.expression)


class TestCalculatorUsage(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_expression_insertion(self):
        self.calculator.digit(1)
        self.calculator.plus()
        self.calculator.digit(2)
        self.assertEqual("1+2", self.calculator.expression)

    def test_compute_result(self):
        self.calculator.expression = "1+2"
        self.assertEqual(3, self.calculator.compute_result())

    def test_compute_result_with_invalid_expression(self):
        self.calculator.expression = "1+"
        with self.assertRaises(ValueError) as context:
            self.calculator.compute_result()
        self.assertEqual("Invalid expression: 1+", str(context.exception))
class Testforcomplexexpression(unittest.TestCase):
    def sqr(self):
        self.calculator.sqr()
        self.calculator.digit(4)
        self.assertEqual("sqrt(4)", self.calculator.expression)
        self.assertEqual("2", self.calculator.compute_result())

    def power(self):
        self.calculator.digit(2)
        self.calculator.power()
        self.calculator.digit(3)
        self.assertEqual("2**3", self.calculator.expression)
        self.assertEqual("8", self.calculator.compute_result())
    
    def op(self):
        self.calculator.op("(")
        self.calculator.digit(3)
        self.calculator.plus()
        self.calculator.digit(1)
        self.assertEqual("(3+1", self.calculator.expression)

    def cp(self):
        self.calculator.digit(3)
        self.calculator.plus()
        self.calculator.digit(1)
        self.calculator.op(")")
        self.assertEqual("3+1)", self.calculator.expression)
import os ; os.environ["KIVY_NO_ARGS"] = "1" # hack for making tests loadable in VS Code
import unittest
from calculator.ui.gui import CalculatorApp


class CalculatorGUITestCase(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()
        self.app._run_prepare()

    def press_button(self, button_text):
        self.app.find_button_by(button_text).trigger_action()

    def assert_display(self, value):
        self.assertEqual(self.app.display.text, value)   

    def tearDown(self):
        self.app.stop()

    def assert_button_exists(self, button_text):
        self.assert_display

    

class TestExpressions(CalculatorGUITestCase):
    def test_integer_expression(self):
        self.press_button("1")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1+2")
        self.press_button("=")
        self.assert_display("3")

    def test_float_expression(self):
        self.press_button("1")
        self.press_button(".")
        self.press_button("2")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1.2+2")
        self.press_button("=")
        self.assert_display("3.2")

class CalculatorGUITestCase(unittest.TestCase):
    # rest of the class is unchanged 

    def assert_button_exists(self, button_text):
        self.assertIsNotNone(self.app.find_button_by(button_text))


class TestLayout(CalculatorGUITestCase):
    buttons_to_test = {
        'C',
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '.', '0', '=', '+',
    }

    def test_initial_display(self):
        self.assert_display("0")

    def test_buttons(self):
        for button_text in self.buttons_to_test:
            with self.subTest(button=button_text):
                self.assert_button_exists(button_text)
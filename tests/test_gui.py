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

class TestC(CalculatorGUITestCase):
    def test_clear_button(self):
        self.press_button("C")

    def test_c_functioning(self):
        self.press_button("3")
        self.press_button("C")
        self.assert_display("0")


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

class TestComplexExpressionIntheGUI(CalculatorGUITestCase):
        def test_gui_buttons(self):
            self.press_button("(")
            self.press_button(")")
            self.press_button("√")
            self.press_button("^")
        def test_gui_complex_expressions(self):
            self.press_button("√")
            self.press_button("1")
            self.press_button("1")
            self.press_button("^")
            self.press_button("2")
            self.press_button(")")
            self.assert_display("sqrt(11**2)")
            self.press_button("=")
            self.assert_display("11.0")
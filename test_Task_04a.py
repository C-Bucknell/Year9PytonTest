import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_04a import main

class TestTask04a(unittest.TestCase):

    @patch('builtins.input', return_value='15')
    @patch('sys.stdout', new_callable=StringIO)
    def test_young_age(self, mock_stdout, mock_input):
        """Test with a young age (example from problem statement)"""
        try:
            main()
            expected_output = "Years until your letter...\n85"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            # The original code has a type error (subtracting integer from string)
            # This test will only pass after the code is fixed
            self.fail("TypeError: The main function has an error with string subtraction")

    @patch('builtins.input', return_value='90')
    @patch('sys.stdout', new_callable=StringIO)
    def test_near_100(self, mock_stdout, mock_input):
        """Test with an age near 100 (example from problem statement)"""
        try:
            main()
            expected_output = "Years until your letter...\n10"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            self.fail("TypeError: The main function has an error with string subtraction")

    @patch('builtins.input', return_value='111')
    @patch('sys.stdout', new_callable=StringIO)
    def test_over_100(self, mock_stdout, mock_input):
        """Test with an age over 100 (example from problem statement)"""
        try:
            main()
            expected_output = "Years until your letter...\n-11"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            self.fail("TypeError: The main function has an error with string subtraction")

    @patch('builtins.input', return_value='100')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exactly_100(self, mock_stdout, mock_input):
        """Test with an age exactly 100"""
        try:
            main()
            expected_output = "Years until your letter...\n0"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            self.fail("TypeError: The main function has an error with string subtraction")

if __name__ == '__main__':
    unittest.main()
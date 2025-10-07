import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_04b import main

class TestTask04b(unittest.TestCase):

    @patch('builtins.input', return_value='75')
    @patch('sys.stdout', new_callable=StringIO)
    def test_under_100(self, mock_stdout, mock_input):
        """Test with age under 100 - should output years until letter"""
        try:
            main()
            expected_output = "Years until your letter...\n25"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            # The original code has a type error (comparing string with integer)
            # This test will only pass after the code is fixed
            self.fail("TypeError: The main function has an error comparing a string with an integer")

    @patch('builtins.input', return_value='111')
    @patch('sys.stdout', new_callable=StringIO)
    def test_over_100(self, mock_stdout, mock_input):
        """Test with age over 100 - should output years since letter"""
        try:
            main()
            expected_output = "You already got your letter 11 years ago"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            # The original code has a type error (comparing string with integer)
            # This test will only pass after the code is fixed
            self.fail("TypeError: The main function has an error comparing a string with an integer")

if __name__ == '__main__':
    unittest.main()
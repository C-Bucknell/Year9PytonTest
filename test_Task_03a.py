import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_03a import main

class TestTask03a(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_very_low_charge(self, mock_stdout, mock_input):
        """Test with charge below 5% (example from problem statement)"""
        try:
            main()
            expected_output = "Connect your charger!"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            # The original code has a type error (comparing string with integer)
            # This test will only pass after the code is fixed
            self.fail("TypeError: The main function has an error comparing a string with an integer")

    @patch('builtins.input', return_value='5')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exactly_5_percent(self, mock_stdout, mock_input):
        """Test with charge exactly at 5% (boundary case)"""
        try:
            main()
            expected_output = "Connect your charger!"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            self.fail("TypeError: The main function has an error comparing a string with an integer")

    @patch('builtins.input', return_value='6')
    @patch('sys.stdout', new_callable=StringIO)
    def test_just_above_5_percent(self, mock_stdout, mock_input):
        """Test with charge just above 5% (boundary case)"""
        try:
            main()
            expected_output = "All good."
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            self.fail("TypeError: The main function has an error comparing a string with an integer")

    @patch('builtins.input', return_value='50')
    @patch('sys.stdout', new_callable=StringIO)
    def test_high_charge(self, mock_stdout, mock_input):
        """Test with high charge (example from problem statement)"""
        try:
            main()
            expected_output = "All good."
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            self.fail("TypeError: The main function has an error comparing a string with an integer")

if __name__ == '__main__':
    unittest.main()
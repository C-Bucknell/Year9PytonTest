import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_03b import main

class TestTask03b(unittest.TestCase):

    @patch('builtins.input', return_value='40')
    @patch('sys.stdout', new_callable=StringIO)
    def test_medium_charge(self, mock_stdout, mock_input):
        """Test with charge between 5% and 50% - should suggest charging soon"""
        try:
            main()
            expected_output = "You should charge your phone soon!"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            # The original code has a type error (comparing string with integer)
            # This test will only pass after the code is fixed
            self.fail("TypeError: The main function has an error comparing a string with an integer")

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_low_charge(self, mock_stdout, mock_input):
        """Test with charge below 5% - should tell user to connect charger"""
        try:
            main()
            expected_output = "Connect your charger!"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        except TypeError:
            # The original code has a type error (comparing string with integer)
            # This test will only pass after the code is fixed
            self.fail("TypeError: The main function has an error comparing a string with an integer")

if __name__ == '__main__':
    unittest.main()
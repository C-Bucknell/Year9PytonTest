import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_01a import main

class TestTask01a(unittest.TestCase):

    @patch('builtins.input', return_value='hello')
    @patch('sys.stdout', new_callable=StringIO)
    def test_example_output(self, mock_stdout, mock_input):
        """Test with the example input 'hello' from the problem statement"""
        main()
        expected_output = "hello hello hello"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='test')
    @patch('sys.stdout', new_callable=StringIO)
    def test_different_input(self, mock_stdout, mock_input):
        """Test with a different input 'test'"""
        main()
        expected_output = "test test test"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        """Test with an empty input string"""
        main()
        expected_output = "  "  # Three spaces when repeating an empty string
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_05 import main

class TestTask05(unittest.TestCase):

    @patch('builtins.input', return_value='4')
    @patch('sys.stdout', new_callable=StringIO)
    def test_four_sheep(self, mock_stdout, mock_input):
        """Test with 4 sheep, as in the first example"""
        main()
        expected_output = "1 sheep\n2 sheep\n3 sheep\n4 sheep"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='9')
    @patch('sys.stdout', new_callable=StringIO)
    def test_nine_sheep(self, mock_stdout, mock_input):
        """Test with 9 sheep, as in the second example"""
        main()
        expected_output = "1 sheep\n2 sheep\n3 sheep\n4 sheep\n5 sheep\n6 sheep\n7 sheep\n8 sheep\n9 sheep"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_one_sheep(self, mock_stdout, mock_input):
        """Test edge case with just 1 sheep"""
        main()
        expected_output = "1 sheep"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_zero_sheep(self, mock_stdout, mock_input):
        """Test edge case with 0 sheep - should print nothing"""
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()
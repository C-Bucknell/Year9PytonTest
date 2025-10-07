import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_06b import main

class TestTask06b(unittest.TestCase):

    @patch('builtins.input', return_value='typo')
    @patch('sys.stdout', new_callable=StringIO)
    def test_word_with_o(self, mock_stdout, mock_input):
        """Test the example case with 'typo' which contains 'o'"""
        main()
        expected_output = "New word!\nt\ny\np\ny\ny\ny\ny\ny\ny\ntypyyyyyy!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='cat')
    @patch('sys.stdout', new_callable=StringIO)
    def test_word_without_o(self, mock_stdout, mock_input):
        """Test a word without 'o' - replacement should not occur"""
        main()
        expected_output = "New word!\nc\na\nt\nt\nt\nt\nt\nt\ncattttt!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='book')
    @patch('sys.stdout', new_callable=StringIO)
    def test_word_with_multiple_o(self, mock_stdout, mock_input):
        """Test a word with multiple 'o's to check all are replaced"""
        main()
        expected_output = "New word!\nb\ny\ny\nk\nk\nk\nk\nk\nk\nbyykkkkk!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='o')
    @patch('sys.stdout', new_callable=StringIO)
    def test_single_letter_o(self, mock_stdout, mock_input):
        """Test with just the letter 'o' as input"""
        main()
        expected_output = "New word!\ny\ny\ny\ny\ny\ny\nyyyyyy!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
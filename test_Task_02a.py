import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_02a import main

class TestTask02a(unittest.TestCase):

    @patch('builtins.input', return_value='Marco!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_input(self, mock_stdout, mock_input):
        """Test with the exact input 'Marco!' - should respond with 'Polo!'"""
        main()
        expected_output = "Polo!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Hello')
    @patch('sys.stdout', new_callable=StringIO)
    def test_wrong_input(self, mock_stdout, mock_input):
        """Test with different input 'Hello' - should not respond"""
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('builtins.input', return_value='Why is this game called Marco! Polo! anyway?')
    @patch('sys.stdout', new_callable=StringIO)
    def test_longer_text(self, mock_stdout, mock_input):
        """Test with longer text containing 'Marco!' - should not respond"""
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('builtins.input', return_value='marco!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_sensitivity(self, mock_stdout, mock_input):
        """Test with lowercase 'marco!' - should not respond (case sensitive)"""
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()
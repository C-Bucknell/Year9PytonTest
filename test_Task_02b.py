import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_02b import main

class TestTask02b(unittest.TestCase):

    @patch('builtins.input', return_value='marco!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_lowercase_input(self, mock_stdout, mock_input):
        """Test with lowercase 'marco!' input"""
        main()
        expected_output = "Polo!"
        # The original code uses title() which won't work for this case
        # This test will fail until the code is fixed
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='mArCo!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_mixed_case_input(self, mock_stdout, mock_input):
        """Test with mixed case 'mArCo!' input"""
        main()
        expected_output = "Polo!"
        # The original code uses title() which won't work for this case
        # This test will fail until the code is fixed
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
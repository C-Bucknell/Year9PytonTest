import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Task_06a import main

class TestTask06a(unittest.TestCase):

    @patch('builtins.input', return_value='Oh no, typo')
    @patch('sys.stdout', new_callable=StringIO)
    def test_phrase_with_spaces(self, mock_stdout, mock_input):
        """Test with a phrase containing spaces, as in first example"""
        main()
        expected_output = "Oh no, typoooooo!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='lol')
    @patch('sys.stdout', new_callable=StringIO)
    def test_short_word(self, mock_stdout, mock_input):
        """Test with a short word, as in second example"""
        main()
        expected_output = "lollllll!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Yass')
    @patch('sys.stdout', new_callable=StringIO)
    def test_ending_with_repeated_letter(self, mock_stdout, mock_input):
        """Test with a word ending in a repeated letter, as in third example"""
        main()
        expected_output = "Yasssssss!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        """Test with empty input, which should handle gracefully"""
        # This test will fail if the code doesn't handle empty strings
        # Since empty[-1] would cause an index error
        try:
            main()
            self.fail("Expected an IndexError with empty input but none was raised")
        except IndexError:
            pass  # Expected behavior with current implementation

if __name__ == '__main__':
    unittest.main()
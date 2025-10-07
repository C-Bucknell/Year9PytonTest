import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the module to test
import Task_07

class TestTask07(unittest.TestCase):
    
    def test_hello_function(self):
        """Test that the hello function returns the correct greeting"""
        result = Task_07.hello("Charlie")
        self.assertEqual(result, "Hello, Charlie")
    
    def test_hello_function_empty(self):
        """Test hello function with empty string"""
        result = Task_07.hello("")
        self.assertEqual(result, "Hello, ")
    
    def test_hello_function_numbers(self):
        """Test hello function with numeric input (as string)"""
        result = Task_07.hello("123")
        self.assertEqual(result, "Hello, 123")
        
    @patch('builtins.input', return_value='Ben')
    @patch('sys.stdout', new_callable=StringIO)
    def test_short_name(self, mock_stdout, mock_input):
        """Test with a short name (less than 3 characters)"""
        Task_07.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your name is too short")
    
    @patch('builtins.input', return_value='Charlie')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_name(self, mock_stdout, mock_input):
        """Test with a valid name (3 or more characters)"""
        Task_07.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, Charlie")
    
    @patch('builtins.input', return_value='Jo')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exactly_2_chars(self, mock_stdout, mock_input):
        """Test with a name exactly 2 characters long"""
        Task_07.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your name is too short")
    
    @patch('builtins.input', return_value='Bob')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exactly_3_chars(self, mock_stdout, mock_input):
        """Test with a name exactly 3 characters long"""
        Task_07.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your name is too short")
    
    @patch('builtins.input', return_value='Alex')
    @patch('sys.stdout', new_callable=StringIO)
    def test_name_with_spaces(self, mock_stdout, mock_input):
        """Test with a name that has 4 letters"""
        Task_07.main()
        # The function should handle the spaces correctly
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, Alex")
    
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_name(self, mock_stdout, mock_input):
        """Test with an empty name"""
        Task_07.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your name is too short")

if __name__ == '__main__':
    unittest.main()
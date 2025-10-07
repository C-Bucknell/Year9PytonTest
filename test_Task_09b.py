import unittest
from unittest.mock import patch
import io
import sys
from Task_09b import main

class TestTask09b(unittest.TestCase):
    # Test 1
    @patch('builtins.input', side_effect=["Dash, Speedy, Lighting, Flash, Sonic", "Dash"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_existing_racer(self, mock_stdout, mock_input):
        """Test removing a racer that exists in the list"""
        main()
        output = mock_stdout.getvalue().strip()
        
        # The output should show all remaining racers in alphabetical order without Dash
        expected_lines = [
            "Remaining racers:", 
            "Flash", 
            "Lighting", 
            "Sonic", 
            "Speedy"
        ]
        actual_lines = output.split('\n')
        self.assertEqual(expected_lines, actual_lines)

    # Test 2
    @patch('builtins.input', side_effect=["Dash, Speedy, Lighting, Flash, Sonic", "Turbo"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_racer_not_in_list(self, mock_stdout, mock_input):
        """Test trying to remove a racer that doesn't exist in the list"""
        main()
        output = mock_stdout.getvalue().strip()
        
        # The output should include the message and all racers in alphabetical order
        expected_lines = [
            "All snails still awake.",
            "Remaining racers:", 
            "Dash", 
            "Flash", 
            "Lighting", 
            "Sonic", 
            "Speedy"
        ]
        actual_lines = output.split('\n')
        self.assertEqual(expected_lines, actual_lines)

    # Test 3
    @patch('builtins.input', side_effect=["Speedy", "Speedy"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_racer_removal(self, mock_stdout, mock_input):
        """Test with a single racer who goes to sleep"""
        main()
        output = mock_stdout.getvalue().strip()
        
        # The output should show no remaining racers
        expected_lines = [
            "Remaining racers:"
        ]
        actual_lines = output.split('\n')
        self.assertEqual(expected_lines, actual_lines)

    # Test 4
    @patch('builtins.input', side_effect=["Flash, Flash, Flash", "Flash"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_duplicate_racers(self, mock_stdout, mock_input):
        """Test with duplicate racers in the list"""
        main()
        output = mock_stdout.getvalue().strip()
        
        # The output should show the remaining racers - only one Flash should be removed
        expected_lines = [
            "Remaining racers:",
            "Flash",
            "Flash"
        ]
        actual_lines = output.split('\n')
        self.assertEqual(expected_lines, actual_lines)

if __name__ == '__main__':
    unittest.main()
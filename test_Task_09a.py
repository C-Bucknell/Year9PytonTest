import unittest
from unittest.mock import patch
import io
import sys
from Task_09a import main

class TestTask09a(unittest.TestCase):
    # Test 1
    @patch('builtins.input', side_effect=["Dash, Speedy, Lighting, Flash, Sonic", "Speedy"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disqualify_racer(self, mock_stdout, mock_input):
        """Test disqualifying a racer that exists in the list"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Speedy has been disqualified!", output)
        self.assertIn("Remaining racers: Dash, Disqualified, Lighting, Flash, Sonic", output)

    # Test 2
    @patch('builtins.input', side_effect=["Dash, Speedy, Lighting, Flash, Sonic", "Gogo"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_racer_not_in_list(self, mock_stdout, mock_input):
        """Test trying to disqualify a racer that doesn't exist in the list"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("All snails still awake.", output)
        self.assertIn("Remaining racers: Dash, Speedy, Lighting, Flash, Sonic", output)

    # Test 3
    @patch('builtins.input', side_effect=["Speedy", "Speedy"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_racer(self, mock_stdout, mock_input):
        """Test with a single racer who gets disqualified"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Speedy has been disqualified!", output)
        self.assertIn("Remaining racers: Disqualified", output)

    # Test 4
    @patch('builtins.input', side_effect=["Flash, Flash, Flash", "Flash"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_duplicate_racers(self, mock_stdout, mock_input):
        """Test with duplicate racers in the list - only first occurrence should be disqualified"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Flash has been disqualified!", output)
        self.assertIn("Remaining racers: Disqualified, Flash, Flash", output)

    # Test 5
    @patch('builtins.input', side_effect=["", "Speedy"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_racer_list(self, mock_stdout, mock_input):
        """Test with an empty racer list"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("All snails still awake.", output)
        self.assertIn("Remaining racers:", output)

    # Test 6
    @patch('builtins.input', side_effect=["Dash, Speedy, Lighting, Flash, Sonic", ""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_sleep_racer(self, mock_stdout, mock_input):
        """Test with an empty sleep racer input"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("All snails still awake.", output)
        self.assertIn("Remaining racers: Dash, Speedy, Lighting, Flash, Sonic", output)

    # Test 7
    @patch('builtins.input', side_effect=["Dash, Speedy, Lighting, Flash, Sonic", "dash"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_sensitivity(self, mock_stdout, mock_input):
        """Test case sensitivity (Dash vs dash)"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("All snails still awake.", output)
        self.assertIn("Remaining racers: Dash, Speedy, Lighting, Flash, Sonic", output)

    # Test 8
    @patch('builtins.input', side_effect=["Disqualified, Speedy, Lighting", "Speedy"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disqualified_already_in_list(self, mock_stdout, mock_input):
        """Test with 'Disqualified' already in the initial list"""
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Speedy has been disqualified!", output)
        self.assertIn("Remaining racers: Disqualified, Disqualified, Lighting", output)

if __name__ == '__main__':
    unittest.main()
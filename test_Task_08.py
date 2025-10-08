import unittest
from unittest.mock import patch
import io
import sys
from Task_08 import main

class TestTask08(unittest.TestCase):
    # Test 1
    @patch('builtins.input', side_effect=["The One Word Wonders", "Song Lyric Ballad"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_basic_functionality(self, mock_stdout, mock_input):
        """Test basic functionality with the example input"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, The One Word Wonders!\nThey will be playing...\n! Song\n! Lyric\n! Ballad\nGive it up for The One Word Wonders!"
        self.assertEqual(output, expected_output)

    # Test 2
    @patch('builtins.input', side_effect=["Lady Gaga", "Paparazzi Applause Shallow"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_second_example(self, mock_stdout, mock_input):
        """Test the second example from the requirements"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, Lady Gaga!\nThey will be playing...\n! Paparazzi\n! Applause\n! Shallow\nGive it up for Lady Gaga!"
        self.assertEqual(output, expected_output)

    # Test 3
    @patch('builtins.input', side_effect=["Solo Artist", "Encore"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_song(self, mock_stdout, mock_input):
        """Test with only one song"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, Solo Artist!\nThey will be playing...\n! Encore\nGive it up for Solo Artist!"
        self.assertEqual(output, expected_output)

    # Test 4
    @patch('builtins.input', side_effect=["No Songs Band", ""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_songs(self, mock_stdout, mock_input):
        """Test with no songs"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, No Songs Band!\nThey will be playing...\nGive it up for No Songs Band!"
        self.assertEqual(output, expected_output)

    # Test 5
    @patch('builtins.input', side_effect=["", "Song1 Song2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_band_name(self, mock_stdout, mock_input):
        """Test with an empty band name"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, !\nThey will be playing...\n! Song1\n! Song2\nGive it up for !"
        self.assertEqual(output, expected_output)

    # Test 6
    @patch('builtins.input', side_effect=["Multi-Word Band", "HitSong1 HitSong2 HitSong3 HitSong4 HitSong5"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_many_songs(self, mock_stdout, mock_input):
        """Test with many songs"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, Multi-Word Band!\nThey will be playing...\n! HitSong1\n! HitSong2\n! HitSong3\n! HitSong4\n! HitSong5\nGive it up for Multi-Word Band!"
        self.assertEqual(output, expected_output)

    # Test 7
    @patch('builtins.input', side_effect=["Special!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~` Chars", "Song1 Song2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_characters(self, mock_stdout, mock_input):
        """Test with special characters in the band name"""
        main()
        output = mock_stdout.getvalue().strip()
        
        expected_output = "Please welcome to the stage, Special!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~` Chars!\nThey will be playing...\n! Song1\n! Song2\nGive it up for Special!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~` Chars!"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
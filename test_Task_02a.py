import unittest
from unittest.mock import patch
from io import StringIO
from Task_02a import main  


class TestTask02a(unittest.TestCase):

    @patch('builtins.input', return_value='Marco!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exact_marco(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Polo!')

    @patch('builtins.input', return_value='Hello')
    @patch('sys.stdout', new_callable=StringIO)
    def test_random_text(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('builtins.input', return_value='marco!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_lowercase_marco(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('builtins.input', return_value='Why is this game called Marco! Polo! anyway?')
    @patch('sys.stdout', new_callable=StringIO)
    def test_long_sentence(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), '')

if __name__ == '__main__':
    try:
        result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTask02a))
        print(f'Tests run: {result.testsRun}')
        print(f'Failures: {len(result.failures)}')
        print(f'Errors: {len(result.errors)}')
    except Exception as e:
        print(f'Test runner encountered an error: {e}')

import unittest
from unittest.mock import patch
from io import StringIO
from Task_02b import main  



class TestTask02b(unittest.TestCase):

    @patch('builtins.input', return_value='mArCo!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_mixed_case_input(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Polo!')

    @patch('builtins.input', return_value='MARCO!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_uppercase_input(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Polo!')

if __name__ == '__main__':
    try:
        result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTask02b))
        print(f'Tests run: {result.testsRun}')
        print(f'Failures: {len(result.failures)}')
        print(f'Errors: {len(result.errors)}')
    except Exception as e:
        print(f'Test runner encountered an error: {e}')

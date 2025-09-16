import unittest
from unittest.mock import patch
from io import StringIO

# Import your main function from the module where it's defined
from Task_01b import main  # Replace 'echo_program' with your actual filename (without .py)

class TestTask01b(unittest.TestCase):

    def run_main_and_capture(self, input_value):
        with patch('builtins.input', return_value=input_value), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            try:
                main()
                return mock_stdout.getvalue().strip()
            except Exception as e:
                return f'EXCEPTION: {e}'

    def test_complete_correct_output(self):
        output = self.run_main_and_capture('hello')
        expected = 'hello hello hello\n\nhello\nhello\nhello'
        self.assertEqual(output, expected, msg=f'Expected exact output but got:\n{output}')

    def test_correct_or_missing_blank_line(self):
        output = self.run_main_and_capture('hello')
        expected_full = 'hello hello hello\n\nhello\nhello\nhello'
        expected_missing_blank = 'hello hello hello\nhello\nhello\nhello'
        self.assertIn(output, [expected_full, expected_missing_blank], msg=f'Output did not match either expected format:\n{output}')

if __name__ == '__main__':
    try:
        result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTask01b))
        print(f'Tests run: {result.testsRun}')
        print(f'Failures: {len(result.failures)}')
        print(f'Errors: {len(result.errors)}')
    except Exception as e:
        print(f'Test runner encountered an error: {e}')

import unittest
from unittest.mock import patch
from io import StringIO

# Import your main function from the module where it's defined
# Replace 'echo_program' with the actual filename (without .py)
from Task_01b import main

class TestEchoProgram(unittest.TestCase):

    def run_main_and_capture(self, input_value):
        with patch('builtins.input', return_value=input_value), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            try:
                main()
                return mock_stdout.getvalue().strip()
            except Exception as e:
                return f'EXCEPTION: {e}'

    def test_partial_or_full_output(self):
        output = self.run_main_and_capture('hello')
        cleaned = output.replace('\n', '')
        expected_full = 'hello hello hello\n\nhello\nhello\nhello'.replace('\n', '')
        expected_partial = 'hello hello hello\n\nhello'.replace('\n', '')
        self.assertIn(cleaned, [expected_full, expected_partial], msg=f'Unexpected output: {output}')

    def test_exact_output(self):
        output = self.run_main_and_capture('hello')
        expected = 'hello hello hello\n\nhello\nhello\nhello'
        self.assertEqual(output, expected, msg=f'Expected exact output but got: {output}')

if __name__ == '__main__':
    # Reset any class-level attributes if needed
    if hasattr(TestEchoProgram, 'first_test_passed'):
        delattr(TestEchoProgram, 'first_test_passed')

    try:
        result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestEchoProgram))
        print(f'Tests run: {result.testsRun}')
        print(f'Failures: {len(result.failures)}')
        print(f'Errors: {len(result.errors)}')
    except Exception as e:
        print(f'Test runner encountered an error: {e}')



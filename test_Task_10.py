import unittest
from Task_10 import format_days

class TestFormatDays(unittest.TestCase):
    #Test 1
    def test_basic_functionality(self):
        """Test basic conversion of short day names to full names"""
        result = format_days('Mon,Tue,Wed')
        self.assertEqual(result, ['Monday','Tuesday','Wednesday'])
    #Test 2
    def test_all_days(self):
        """Test all seven days of the week"""
        result = format_days('Mon,Tue,Wed,Thu,Fri,Sat,Sun')
        self.assertEqual(result, ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    #Test 3
    def test_single_day(self):
        """Test a single day conversion"""
        result = format_days('Fri')
        self.assertEqual(result, ['Friday'])
    #Test 4
    def test_unknown_day(self):
        """Test handling of an unknown day name"""
        result = format_days('Mon,Fun,Wed')
        self.assertEqual(result, ['Monday','Wednesday'])
    #Test 5
    def test_all_unknown_days(self):
        """Test case where all day names are invalid"""
        result = format_days('Fun,Day,Week')
        self.assertEqual(result, [])
    #Test 6
    def test_empty_string(self):
        """Test an empty string input"""
        result = format_days('')
        self.assertEqual(result, [])
    #Test 7
    def test_mixed_valid_invalid(self):
        """Test a mix of valid and invalid day names"""
        result = format_days('Mon,Invalid,Tue,123,Fri')
        self.assertEqual(result, ['Monday','Tuesday','Friday'])
    #Test 8
    def test_repeated_days(self):
        """Test handling of repeated day names"""
        result = format_days('Mon,Mon,Tue,Tue')
        self.assertEqual(result, ['Monday','Monday','Tuesday','Tuesday'])
    #Test 9        
    def test_weekend_days(self):
        """Test weekend days"""
        result = format_days('Sat,Sun')
        self.assertEqual(result, ['Saturday','Sunday'])
    #Test 10 
    def test_weekday_days(self):
        """Test weekday days"""
        result = format_days('Mon,Tue,Wed,Thu,Fri')
        self.assertEqual(result, ['Monday','Tuesday','Wednesday','Thursday','Friday'])
    #Test 11    
    def test_reverse_order(self):
        """Test days in reverse order"""
        result = format_days('Sun,Sat,Fri,Thu,Wed,Tue,Mon')
        self.assertEqual(result, ['Sunday','Saturday','Friday','Thursday','Wednesday','Tuesday','Monday'])
    #Test 12    
    def test_random_order(self):
        """Test days in random order"""
        result = format_days('Wed,Mon,Sat,Tue,Fri,Sun,Thu')
        self.assertEqual(result, ['Wednesday','Monday','Saturday','Tuesday','Friday','Sunday','Thursday'])

if __name__ == '__main__':
    unittest.main()
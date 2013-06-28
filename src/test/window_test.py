import unittest
from programa.windows import BusinessWindow
import datetime

class WindowTest(unittest.TestCase):
            
    def setUp(self):
        self.window = BusinessWindow()
        self.window.add_period(8, 12);
        
    def test_adding_one_period(self):
        self.assertEqual(1, len(self.window.periods))
        
    def test_adding_the_same_period(self):
        self.window.add_period(8, 12);
        self.assertEqual(1, len(self.window.periods))
        
    def test_adding_two_periods(self):
        self.window.add_period(14, 18);
        self.assertEqual(2, len(self.window.periods))
        
    def test_when_window_has_the_date(self):
        date = datetime.datetime(2012, 3, 20, 11, 0, 0)
        self.assertTrue(self.window.has(date))
        
    def test_when_window_has_the_date_2(self):
        date = datetime.datetime(2012, 3, 20, 11, 0, 0)
        self.assertFalse(self.window.does_not_have(date))
        
    def test_when_window_dosent_have_the_date_time(self):
        date = datetime.datetime(2012, 3, 20, 20, 0, 0)
        self.assertFalse(self.window.has(date))
        
    def test_window_dosent_have_weekends(self):
        date = datetime.datetime(2013, 3, 23, 9, 0, 0)
        self.assertFalse(self.window.has(date))
        
    def test_when_window_dosent_have_the_date_time_2(self):
        date = datetime.datetime(2012, 3, 20, 20, 0, 0)
        self.assertTrue(self.window.does_not_have(date))
        
    def test_window_dosent_have_weekends_2(self):
        date = datetime.datetime(2013, 3, 23, 9, 0, 0)
        self.assertTrue(self.window.does_not_have(date))

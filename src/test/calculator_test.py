from programa.calculators import Calculator
from programa.windows import BusinessWindow
import datetime
import unittest


class CalculatorTest(unittest.TestCase):
    def setUp(self):        
        self.window = BusinessWindow()
        self.window.add_period(8, 12) 
        self.window.add_period(14, 18)
        
        self.calc = Calculator()
        
    def testIdealCenario(self):
        initial = datetime.datetime(2010, 07, 16, 8, 0, 0)
        final = datetime.datetime(2010, 07, 16, 18, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(8, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testBrokenMorning(self):
        initial = datetime.datetime(2010, 07, 16, 10, 30, 0)
        final = datetime.datetime(2010, 07, 16, 18, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(5, time.hours)
        self.assertEquals(30, time.minutes)
        
    def testBrokenAfterNoon(self):
        initial = datetime.datetime(2010, 07, 16, 14, 0, 0)
        final = datetime.datetime(2010, 07, 16, 17, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(3, time.hours)
        self.assertEquals(0, time.minutes)
        
        
    def testBrokenMorningAndAfternoon(self):
        initial = datetime.datetime(2010, 07, 16, 9, 0, 0)
        final = datetime.datetime(2010, 07, 16, 17, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(6, time.hours)
        self.assertEquals(0, time.minutes)
        
        
    def testEndingMorningEarlyAfternoon(self):
        initial = datetime.datetime(2010, 07, 16, 11, 50, 0)
        final = datetime.datetime(2010, 07, 16, 13, 55, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(0, time.hours)
        self.assertEquals(10, time.minutes)
        
        
    def testEndingAfternonnAfterWindow(self):
        initial = datetime.datetime(2010, 07, 16, 14, 45, 0, 0)
        final = datetime.datetime(2010, 07, 16, 18, 55, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(3, time.hours)
        self.assertEquals(15, time.minutes)
        
    def testEarlyAfternoonAfterWindow(self):
        initial = datetime.datetime(2010, 07, 16, 13, 15, 0)
        final = datetime.datetime(2010, 07, 16, 18, 55, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(4, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testIdeialCenario2Between2Days(self):
        initial = datetime.datetime(2010, 07, 15, 8, 0, 0)
        final = datetime.datetime(2010, 07, 16, 18, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(16, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testBeforeWindowBetween2Days(self):
        initial = datetime.datetime(2010, 07, 15, 7, 45, 0)
        final = datetime.datetime(2010, 07, 16, 18, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(16, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testAfterWindowBetween2Days(self):
        initial = datetime.datetime(2010, 07, 15, 18, 45, 0)
        final = datetime.datetime(2010, 07, 16, 18, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(8, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testBetween2Days(self):
        initial = datetime.datetime(2010, 07, 15, 11, 45, 0)
        final = datetime.datetime(2010, 07, 16, 14, 15, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(8, time.hours)
        self.assertEquals(30, time.minutes)
        
    def testBetween5Days(self):
        initial = datetime.datetime(2010, 07, 11, 11, 1, 0)
        final = datetime.datetime(2010, 07, 19, 14, 59, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(1, time.days)
        self.assertEquals(20, time.hours)
        self.assertEquals(59, time.minutes)
        
    def testBetween20Days(self):
        initial = datetime.datetime(2010, 07, 1, 8, 0, 0)
        final = datetime.datetime(2010, 07, 21, 18, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(5, time.days)
        self.assertEquals(0, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testIdealCenario2(self):
        initial = datetime.datetime(2010, 7, 12, 17, 51, 0)
        final = datetime.datetime(2010, 7, 13, 11, 51, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(4, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testIdealCenario3(self):
        initial = datetime.datetime(2010, 7, 12, 17, 50, 0)
        final = datetime.datetime(2010, 7, 13, 11, 51, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(4, time.hours)
        self.assertEquals(1, time.minutes)
        
    def testBetween5Days2(self):
        initial = datetime.datetime(2010, 07, 19, 11, 1, 0)
        final = datetime.datetime(2010, 07, 20, 14, 59, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(9, time.hours)
        self.assertEquals(58, time.minutes)
        
    def testBetweenYears(self):
        initial = datetime.datetime(2009, 12, 31, 14, 0, 0)
        final = datetime.datetime(2010, 1, 1, 12, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(8, time.hours)
        self.assertEquals(0, time.minutes)
        
    def testBetweenWeekends(self):
        initial = datetime.datetime(2010, 7, 9, 20, 0, 0)
        final = datetime.datetime(2010, 7, 12, 8, 1, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(0, time.hours)
        self.assertEquals(1, time.minutes)
        
    def testRandom01(self):
        initial = datetime.datetime(2012, 6, 4, 11, 35, 0)
        final = datetime.datetime(2012, 6, 4, 11, 37, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(0, time.hours)
        self.assertEquals(2, time.minutes)

    def testRandom02(self):
        initial = datetime.datetime(2012, 6, 4, 8, 58, 0)
        final = datetime.datetime(2012, 6, 14, 14, 35, 0, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(2, time.days)
        self.assertEquals(19, time.hours)
        self.assertEquals(37, time.minutes)
        
    def testRandom03(self):
        initial = datetime.datetime(2012, 6, 4, 8, 58, 0)
        final = datetime.datetime(2012, 6, 4, 8, 58, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(0, time.hours)
        self.assertEquals(0, time.minutes)
        
        
    def testRandom04(self):
        initial = datetime.datetime(2012, 6, 4, 7, 32, 0)
        final = datetime.datetime(2012, 6, 4, 7, 55, 0)
        
        time = self.calc.time_between(initial, final, self.window)
        
        self.assertEquals(0, time.days)
        self.assertEquals(0, time.hours)
        self.assertEquals(0, time.minutes)        

import unittest
from programa.periods import Period


class PeriodTest(unittest.TestCase):

    def setUp(self):
        self.period = Period(8,10)
    
    def testWhenCreatingAPeriod(self):
        period = Period(8,10)
        self.failUnless(period.start == 8)
        self.failUnless(period.end == 10)        
        
    def testWhenCreatingAPeriodWithEndGreaterThenStart(self):
        self.assertRaises(Exception, Period, (10,8))
        
    def testEqualityOfEqualPeriods(self):
        self.assertTrue(self.period == Period(8,10))
        
    def testEqualityOfDiferentsPeriods(self):    
        self.assertFalse(self.period == Period(8,11))
        self.assertFalse(self.period == Period(7,10))

    

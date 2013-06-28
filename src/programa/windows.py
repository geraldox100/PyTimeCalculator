from periods import Period

class BusinessWindow():
    
    
    def __init__(self):
        self.periods = []
    
    def add_period(self, start, end):
        periods = self.periods
        new = Period(start, end)
        if new not in periods:
            periods.append(new)
        
    def has(self, date):
        if date.weekday() < 5:
            for p in self.periods:
                if date.hour >= p.start and date.hour < p.end:
                    return True            
                
        return False
    
    def does_not_have(self, date):
        return not self.has(date)

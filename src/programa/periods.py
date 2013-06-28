class Period:
    def __init__(self, start, end):
        if(end < start):
            raise Exception("'start' (%d) must be grater then 'end' (%d)" % (start, end))
        self.start = start
        self.end = end
        
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    

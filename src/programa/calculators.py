from programa.time import Time
from datetime import timedelta




class Calculator():
    
    def time_between(self, initial_date, final_date, window):
        hours_worked = 0
        initial_minutes = 0
        final_minutes = 0
        
        if self.dates_are_diferent(initial_date, final_date):
            initial_minutes = self.ajust_initial_minutes(initial_date, window)
            final_minutes = self.ajust_final_minutes(final_date, window)
        else:
            initial_minutes = final_date.minute
            final_minutes = initial_date.minute * -1
            
        initial_date = initial_date + timedelta(minutes=initial_minutes)
        
        while self.dates_are_diferent(initial_date, final_date) and initial_date < final_date:
            if  window.has(initial_date) :
                hours_worked += 1
                
            initial_date = initial_date + timedelta(hours=1)
            
        return self.time_builder(hours_worked, initial_minutes, final_minutes)
    
    def time_builder(self, hours, initial_minutes, final_minutes):
        days = hours / 24
        
        hours = hours % 24
        hours += (initial_minutes + final_minutes) / 60
        
        minutes = (initial_minutes + final_minutes) % 60
        
        return Time(days, hours, minutes)
    
    def dates_are_diferent(self, inicial, final):
        if (inicial.hour != final.hour and inicial.hour < final.hour):
            return True
        if (inicial.day != final.day):
            return True
        if (inicial.month != final.month):
            return True
        if (inicial.year != final.year):
            return True
        return False
    
    def ajust_initial_minutes(self, initial_date, window):
        initial_minutes = initial_date.minute
        if window.does_not_have(initial_date):
            initial_minutes = 0
        else:
            if initial_minutes > 0 :
                initial_minutes = 60 - initial_minutes
                
        return initial_minutes
    
    def ajust_final_minutes(self, final_date, janela):
        final_minutes = final_date.minute
        if janela.does_not_have(final_date):
            final_minutes = 0
        return final_minutes

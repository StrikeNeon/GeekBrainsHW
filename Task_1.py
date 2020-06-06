# -*- coding: utf-8 -*-
class Date():
    def __init__(self, date):
        try:
            self.date = date
            if Date.validate(Date.transform(self.date)) == True:
                self.date_data = Date.transform(self.date)  
        except TypeError:
            print("a date has to be a day-month-year formatted string")
    
    @classmethod
    def transform(cls, date):
        day, month, year = int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2])
        return day, month, year
    
    @staticmethod
    def validate(date):
        if date[0] < 1 or date[0] >31:
            raise ValueError("day must be in rage 1-31")
            return False
        if date[1] < 1 or date[1] >12:
            raise ValueError("month must be in range 1-12")
            return False
        if date[2] %4==0 and date[1] == 2 and date[0] >29:
            raise ValueError(f"year {date[2]} is a leap year, there are 29 days in a leap year")
            return False
        elif date[2] %100==0 and date[1] == 2 and date[0] >29:
            raise ValueError(f"year {date[2]} is a leap year, there are 29 days in a leap year")
            return False
        elif date[2] %400==0 and date[1] == 2 and date[0] >29:
            raise ValueError(f"year {date[2]} is a leap year, there are 29 days in a leap year")
            return False
        else: 
            return True
    
print(Date("3-2-2020").date_data)
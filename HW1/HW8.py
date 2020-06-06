# -*- coding: utf-8 -*-

#1

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

#2
class ZeroDiv(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return self.message
        else:
            return "element is not a number"
        
a,b = 10, 2
if b ==0:
    raise ZeroDiv("divided by zero")
else: print(a/b)

#3
class NaN(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return self.message
        else:
            return "element is not a number"
        
#lis = []
#while True:
#    el = input("enter number ")
#    if el != "stop":
#        try:
#            el = int(el)
#            lis.append(el)
#        except ValueError:
#            raise NaN()
#    else:
#        break
    
#4-6
import os
import json

class OfficeWarehouse():
    def __init__(self):
        self.dir = os.getcwd()
        self.DB_temp = {}
        if not os.path.exists('DB_Saved'):
            os.makedirs('DB_Saved')
        self.DB_loc =  os.path.join(self.dir, 'DB_Saved')
        self.count = 0
        print(self.DB_loc)
    
    def __str__(self):
        return "Base office equipment class"
    
    def __save(self):
        with open(os.path.join(self.DB_loc, 'DB_file.json'), "w") as write_file:
            json.dump(self.DB_temp, write_file)
    
    @staticmethod
    def validate_data(typ, *param):
        print(param)
        if typ == "printer":
            try:
                record = Printer({"model":param[0][0], "printtype":param[0][1], "printspeed":int(param[0][2]), "interface":param[0][3], "price":int(param[0][4])}).parameters
                return record
            except TypeError:
                return None
        if typ == "scanner":
            try:
                record = Scanner({"model":param[0][0], "scanspeed":int(param[0][1]), "interface":param[0][2], "price":int(param[0][3])}).parameters
                return record
            except TypeError:
                return None
        if typ == "scanner":
            try:
                record = Scanner({"model":param[0][0], "scanspeed":int(param[0][1]), "printtype":int(param[0][2]), "interface":param[0][3], "price":int(param[0][4])}).parameters
                return record
            except TypeError:
                return None
            
    def record(self):
        record = {"Equipment_type":None, "Quantity":None, "Parameters":None}
        command = input(f'''
current record is {record}
input Equipment type and Quantity
format: Type Quantity
                        ''')
        if command.split()[0] not in ["printer","scanner","xerox"]:
            return f'Equipment type mismatch: you entered {command.split()[0]}, only printer, scanner and xerox are supported'
        else:
            record["Equipment_type"] = command.split()[0]
            try:
              record["Quantity"] = int(command.split()[1])
            except TypeError:
                return False
        if command.split()[0] == "printer":
            try:
                model, printtype, printspeed, interface, price = input("""
input parameters
format: model, printtype, 
printspeed, interface, price
                                                                       """).split()
                record["Parameters"] = OfficeWarehouse.validate_data("printer", (model, printtype, printspeed, interface, price))
            except IndexError:print("record incomplete")

        elif command.split()[0] == "scanner":
            try:
                model, scanspeed, interface, price = input("""
input parameters
format: model, scanspeed, 
interface, price
                                                           """).split()
                record["Parameters"] = OfficeWarehouse.validate_data("scanner", (model, scanspeed, interface, price))
            except IndexError:print("record incomplete")
        elif command.split()[0] == "xerox":
            try:
                model, scanspeed, printspeed, interface, price = input("""
input parameters
format: model, scanspeed, 
printspeed, interface, price
                                                                       """).split()
                record["Parameters"] = OfficeWarehouse.validate_data("xerox", (model, scanspeed, printspeed, interface, price))
            except IndexError:print("record incomplete")
        
        if record["Parameters"]:
            command = input(f'''
current record is {record}
save or discard record?
                            ''')
            if command == "save":
                self.DB_temp[self.count]=record
                self.count +=1
                self.__save()
            elif command == "discard":
                return False
            else:
                print("invalid command")
        else: print("Data invalid")
        

class OfficeEq():
    def __init__(self, parameters):
        self.parameters = parameters
    def __str__(self):
        return "Base office equipment class"

class Printer(OfficeEq):
    def __init__(self, parameters):
        try:
            OfficeEq.__init__(self,parameters)
            self.model = self.parameters["model"]
            self.printtype = self.parameters["printtype"]
            self.printspeed = self.parameters["printspeed"]
            self.interface = self.parameters["interface"]
            self.price = self.parameters["price"]
        except KeyError:
            raise
class Scanner(OfficeEq):
    def __init__(self, parameters):
        try:
            OfficeEq.__init__(self,parameters)
            self.model = self.parameters["model"]
            self.scanspeed = self.parameters["scanspeed"]
            self.interface = self.parameters["interface"]
            self.price = self.parameters["price"]
        except KeyError:
            raise
    def __str__(self):
        return "Scanner equipment class"
    
class Xerox(OfficeEq):
    def __init__(self, parameters):
        try:
            OfficeEq.__init__(self,parameters)
            self.model = self.parameters["model"]
            self.scanspeed = self.parameters["scanspeed"]
            self.printspeed = self.parameters["printspeed"]
            self.interface = self.parameters["interface"]
            self.price = self.parameters["price"]
        except KeyError:
            raise
    def __str__(self):
        return "Scanner equipment class"

print(OfficeEq({'a':1}).parameters)
print(Scanner({"model":1, "scanspeed":5, "interface":"usb", "price":500}).parameters)
site1 = OfficeWarehouse()
site1.record()
print(site1.DB_temp)

#7
class ComplexNum():
    def __init__(self, real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
    def __add__(self, other):
        return ComplexNum(self.real+other.real,self.imaginary+other.real)
    def __mul__(self, other):
        return ComplexNum((self.real*other.real) - (self.imaginary*other.imaginary), (self.real*self.imaginary)+(other.real*other.imaginary))
    
num1 = ComplexNum(3, 2)
num2 = ComplexNum(3, 1)
print(num1+num2)
print(num1*num2)
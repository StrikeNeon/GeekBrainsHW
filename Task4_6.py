# -*- coding: utf-8 -*-
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
        self.loaded = None
    
    def __str__(self):
        return "Base office equipment class"
    
    def __save(self):
        with open(os.path.join(self.DB_loc, 'DB_file.json'), "w") as write_file:
            json.dump(self.DB_temp, write_file)
            
    def load(self):
        try:
            with open(os.path.join(self.DB_loc, 'DB_file.json'), "r") as read_file:
                self.loaded = json.load(read_file)
        except FileNotFoundError:
            print("Nothing to load")
            
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
format: 
Type Quantity
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
format: 
model, printtype, 
printspeed, interface, price
                                                                       """).split()
                record["Parameters"] = OfficeWarehouse.validate_data("printer", (model, printtype, printspeed, interface, price))
            except IndexError:print("record incomplete")

        elif command.split()[0] == "scanner":
            try:
                model, scanspeed, interface, price = input("""
input parameters
format:
model, scanspeed, 
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
current record is 
{record}
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
site1.load()
site1.record()
print(site1.loaded)
import table as t
import csv

class DrinksRound:         
    order = []

    def update_order(self, name, drink):
        self.name = name
        self.drink = drink        
        self.order.append([self.name, self.drink])        
        return self.order  
              
    def print_order(self):     
        t.print_round_table("drinks order", self.order)
    
    def save_order(self):
        with open("drinksorder.csv", "w", newline = "") as order_file:
            write_file = csv.writer(order_file, quoting=csv.QUOTE_ALL)
            for item in self.order:
                write_file.writerow(item)

    def load_order(self):        
        with open("drinksorder.csv", "r") as order_file:
            order_list = list(csv.reader(order_file))
        return order_list
           
class Info:
    def __init__(self):
        self.info_db = {}     
    
    def update_dictionary(self, name, drink, milk):
        self.name = name 
        self.drink = drink
        self.milk = milk              
        self.info_db.update({len(self.info_db) + 1: [self.name, self.drink, self.milk]})
        return self.info_db

    def info_table(self):
        t.print_info_table("saved info", self.info_db.values())
        for value in self.info_db.values():
            print(f"{value[0]} | {value[1]}, {value[2]} |")

# class RoundMenu(DrinksRound):    
    

#     def rounds_menu(self): 
#         order_list = super().order 
#         name_add = str(input("Enter a name: ")).title()
#         drink_add = str(input("Enter a drink: ")).lower()
#         order_list.update_order(name_add, drink_add)      
#         self.round_list.print_order() 
#         cancel = exit_option()
#         self.round_list.save_order()
#         while cancel != "x":            
#             name_add = str(input("Enter a name: ")).title()
#             drink_add = str(input("Enter a drink: ")).lower()
#             self.round_list.update_order(name_add, drink_add)        
#             self.round_list.print_order()
#             cancel = exit_option()
#             self.round_list.save_order() 

#     def round_table(self):
#         drinks_round = c.DrinksRound()    
#         t.print_round_table("drinks order", drinks_round.load_order())
    
# stuff = Info()
# stuff.update_dictionary("Khalid", "coffee", "almond milk")
# print(stuff.info_db)
# stuff.info_table()
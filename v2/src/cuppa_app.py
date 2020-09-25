import table as t
import cuppa_class as c

# Defines expect commands
GET_INFO = "1"
UPDATE_DRINKS_ROUND = "2"
VIEW_DRINKS_ROUND = "3"
EXIT_APP = "4"

SELECTION_MENU = """
Welcome to Cuppa!
Please selection an option:

[1] View saved information
[2] Create a round of drinks
[3] View your round
[4] Exit
 """

# Pauses the script in between commands
def wait():
    input("Press ENTER to continue.\n")

def exit_option():
    return str(input("\nPress ENTER to continue.\nPress x to cancel.\n")).lower()

# Put the initial menu in a function so that it can be called within itself
def menu():
    print(SELECTION_MENU)
    user_input = str(input())
    if __name__ == "__main__":
        while True:
                
            if user_input == GET_INFO:
                info_menu()         

            elif user_input == UPDATE_DRINKS_ROUND:
                rounds_menu()
                wait()            
                menu()
            
            elif user_input == VIEW_DRINKS_ROUND:
                round_table()
                wait()
                menu()

            elif user_input == EXIT_APP:
                print("See you next time.")
                exit()
            
            else:
                print("That's not a valid option.")
                exit()

# Function that creates a loop to for the user to add multiple drink orders
# to a list
def rounds_menu():
    round_handler = c.DrinksRound()    
    name_add = str(input("Enter a name: ")).title()
    drink_add = str(input("Enter a drink: ")).lower()
    round_handler.update_order(name_add, drink_add)      
    round_handler.print_order() 
    cancel = exit_option()
    round_handler.save_order()
    while cancel != "x":            
        name_add = str(input("Enter a name: ")).title()
        drink_add = str(input("Enter a drink: ")).lower()
        round_handler.update_order(name_add, drink_add)        
        round_handler.print_order()
        cancel = exit_option()
        round_handler.save_order()       

# Function that print a table containing the orders saved to drinksorder.csv        
def round_table():
    drinks_round = c.DrinksRound()    
    t.print_round_table("drinks order", drinks_round.load_order())

def info_menu():
    info_handler = c.Info()
    info_handler.info_table()
    update_option = str(input("\nWould you like to save a preference?\ny or n\n"))
    if update_option == "y":                   
        name_add = str(input("Enter a name: ")).title()
        drink_add = str(input("Enter a drink: ")).lower()
        milk_add = str(input("Enter a milk preference: ")).lower()
        info_handler.update_dictionary(name_add, drink_add, milk_add)
        info_handler.info_table()
        while True: 
            cancel = exit_option()
            if cancel == "x":             
                menu()
            else:
                name_add = str(input("Enter a name: ")).title()
                drink_add = str(input("Enter a drink: ")).lower()
                milk_add = str(input("Enter a milk preference: ")).lower()
                info_handler.update_dictionary(name_add, drink_add, milk_add)
                info_handler.info_table()                
    elif update_option == "n":
        menu()
    else:
        print("That's not a valid input.")

menu()
    
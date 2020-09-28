import load_save as l 
import table as t
import cuppa_classes as c
#defines expected commands
GET_NAMES = "1"
GET_DRINKS = "2"
ASSIGN_DRINK = "3"
VIEW_FAV_DRINKS = "4"
REMOVE_DRINK_PREF = "5"
CREATE_A_ROUND = "6"
VIEW_ROUND = "7"
RUN_AWAY = "0"
MENU = f"""
Welcome to Round O' Drinks!
Create rounds for your mates and save their
preferences!
Please select a database to choose from:

[{GET_NAMES}] People 
[{GET_DRINKS}] Drinks
[{ASSIGN_DRINK}] Assign favourite drinks
[{VIEW_FAV_DRINKS}] View favourite drinks
[{REMOVE_DRINK_PREF}] Remove favourite drink
[{CREATE_A_ROUND}] Create a round
[{VIEW_ROUND}] View your round
[{RUN_AWAY}] Exit
"""

def selection_screen():
    print(MENU)

# Separate functions to ensure names don't end up in the drinks list and vice versa.
def user_input():
    return str(input())  

def name_input():
    return str(input("Please enter a name:\n")).title()

def drink_input():
    return str(input("Please enter a drink:\n")).lower()

# Pauses the script in the middle of the while loop
def wait():
    input("Press ENTER to continue\n")

# Deletes item from a list
def delete_item(list, item):
    list.remove(item)

def who_is_serving():
    return str(input("Who is making the round?\n"))
    
 
 
def name_selector():
    t.print_table("names", name_list)
    person_select = str(input("Please type a name from the database:\n")).title()        
    if person_select in name_list:
        return person_select 
    else:
        print("\nOne of your options is not in the database.\n")
        name_selector()
    

def drink_selector():
    t.print_table("drinks", drinks_list)
    drink_select = str(input("Please assign a drink from the database:\n")).lower()
    if drink_select in drinks_list:
        return drink_select
    else:
        print("\nOne of your options is not in the database.\n")
        drink_selector()  

def make_a_combo():
    choice1 = name_selector()
    choice2 = drink_selector() 
    return choice1 + " - " + choice2   
     
# def create_an_order():
#     name_add = name_input()
#     drink_add = drink_input()
#     round_list.append(f"{name_add} ordered {drink_add}")
#     t.print_table(f"{server_list[0]} is making the round", round_list)

# def round_maker_loop():
#     while True:
#         continue_option = str(input("\nPress ENTER to continue or x to save and exit.\n"))
#         if continue_option == "x":
#             l.save_stuff("drinksround.csv", round_list)
#             wait()
#         else:
#             create_an_order()

def option_1():
    t.print_table("names", name_list)
    add_name_option = str(input("\nWould you like to edit this database?\n[1] Add name\n[2] Remove name\n[3] Return to menu\n"))
    if add_name_option == "1":
        x = name_input()
        name_to_add = c.Names(x)
        name_to_add.name_add(name_list)
        option_1()      
    elif add_name_option == "2":
        y = name_input()
        name_to_del = c.Names(y)
        name_to_del.del_name(name_list)
        option_1()
    elif add_name_option == "3":        
        wait()
    else:
        print("That's not a valid option.")
        option_1()
        

def option_2():
    t.print_table("drinks", drinks_list)
    add_drink_option = str(input("\nWould you like to edit this database?\n[1] Add drink\n[2] Remove drink\n[3] Return to menu\n"))
    if add_drink_option == "1":
        x = drink_input()
        drink_to_add = c.Drink(x)
        drink_to_add.drink_add(drinks_list)
        option_2()
    elif add_drink_option == "2":
        y = drink_input()
        drink_to_del = c.Drink(y)
        drink_to_del.del_drink(drinks_list)
        option_2()            
    elif add_drink_option == "3":
        wait()
    else:
        print("That's not a valid option.")
        option_2()

def option_3():
    assigned_drink = make_a_combo()
    if assigned_drink not in fav_drinks_list:
        fav_drinks_list.append(assigned_drink)
        t.print_table("fav drinks", fav_drinks_list)
    else:
        print("That combination has already been done.")
        option_3() 

def option_4():
    t.print_table("fav drinks", fav_drinks_list)
    del_assigned_drink = make_a_combo()
    if del_assigned_drink in fav_drinks_list:
        delete_item(fav_drinks_list, del_assigned_drink)
        l.save_stuff("favdrinks.csv", fav_drinks_list)
    else:
        print("That combination does not exist.")
        option_4()

def option_5():
    t.print_table("fav drinks", fav_drinks_list)
    del_assigned_drink = make_a_combo()
    if del_assigned_drink in fav_drinks_list:
        delete_item(fav_drinks_list, del_assigned_drink)        
    else:
        print("That combination does not exist.")
        option_5()

def option_6():
    t.print_table("fav drinks", fav_drinks_list)
    wait()

def option_7():    
    server = who_is_serving()
    name = name_selector()
    drink = drink_selector()
    order1 = c.RoundMaker(name, drink, round_list)
    order1.create_an_order(server)
    exit_selection = str(input("\nWould you like to continue?\n[1] Yes\n[2] No\n"))
    if exit_selection == "1" or exit_selection == "2":
        while exit_selection != "2":
            name = name_selector()
            drink = drink_selector()
            order2 = c.RoundMaker(name, drink, round_list)
            order2.create_an_order(server)
            exit_selection = str(input("\nWould you like to continue?\n[1] Yes\n[2] No\n"))
    else:
        print("That ain't a valid command buster.")
        option_7()
    
        



    # t.print_table(f"{server_list[0]} is making the round", round_list)
    # create_an_order()
    # round_maker_loop()

def option_8():
    loaded_order = c.RoundMaker(round_list)
    loaded_order.load_order()
    t.print_table("BOW BEFORE YOUR NEW GOD", loaded_order.order_list)
    # t.print_table(f"{server_list[0]} is making the round", round_list)
    # wait() 

name_list = l.load_stuff("pubnames.csv")
drinks_list = l.load_stuff("drinksmenu.csv")
fav_drinks_list = l.load_stuff("favdrinks.csv")
load_round = l.load_stuff("drinksround.csv")
round_list = c.RoundMaker().order_list


def ultimate_menu():
    while True:           
        selection_screen()
        user_selection = user_input()
        # Organises arguments based on user input
        if user_selection == GET_NAMES:        
            option_1()
            ultimate_menu()

        elif user_selection == GET_DRINKS:        
            option_2()   
            ultimate_menu()

        elif user_selection == ASSIGN_DRINK:
            option_3()
            l.save_stuff("favdrinks.csv", fav_drinks_list)
            ultimate_menu()                
                                
        elif user_selection == REMOVE_DRINK_PREF:              
            option_5()
            l.save_stuff("favdrinks.csv", fav_drinks_list)
            wait()
            ultimate_menu()
                    
        elif user_selection == VIEW_FAV_DRINKS:          
            option_6()
            ultimate_menu()

        elif user_selection == CREATE_A_ROUND:
            option_7()
            l.save_stuff("drinksround.csv", round_list)            
            ultimate_menu()
        
        elif user_selection == VIEW_ROUND:
            option_8()
            ultimate_menu()        

        elif user_selection == RUN_AWAY:
            l.save_stuff("pubnames.csv", name_list)
            l.save_stuff("drinksmenu.csv", drinks_list)
            print("We hope you enjoyed your stay.")
            exit()     
        else:
            print(f"{str(user_selection)} is not a valid command.\n")
            wait()
            ultimate_menu()
                    
                    

ultimate_menu()
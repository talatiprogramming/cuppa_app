import load_save as l 
import table as t

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

def name_add():         
    new_name = name_input()                                   
    if new_name.isalpha() == False:
        print("You can't add that to the database.\n")
        name_add()
    elif new_name in pub_name_list:
        print("That entry already exists.\nPlease enter a unique name into the database.")
        name_add()
    else:   
        pub_name_list.append(new_name)    
        t.print_table("names", pub_name_list)
        l.save_stuff("pubnames.csv", pub_name_list)
        wait()

def del_name():
    name_del = name_input()        
    if name_del in pub_name_list:
        delete_item(pub_name_list, name_del)               
        t.print_table("names", pub_name_list)
        l.save_stuff("pubnames.csv", pub_name_list)
        wait()
    else:
        print("I can't find that in the database.\n")
        del_name()

def drink_add():
    new_drink = drink_input()
    if new_drink.isalpha() == False:
        print("You can't add that to the this database.\n")
        drink_add()
    elif new_drink in drinks_menu_list:
        print("That entry already exists.\nPlease enter a unique drink into the database.")
        drink_add()
    else:            
        drinks_menu_list.append(new_drink)
        t.print_table("drinks", drinks_menu_list)
        l.save_stuff("drinksmenu.csv", drinks_menu_list)
        wait()

def del_drink():
    drink_del = drink_input() 
    if drink_del in drinks_menu_list:
        delete_item(drinks_menu_list, drink_del)               
        t.print_table("drinks", drinks_menu_list)
        l.save_stuff("drinksmenu.csv", drinks_menu_list)
        wait()                
    else:
        print("I can't find that in the database.")
        del_drink()
  
 
def name_selector():
    t.print_table("names", pub_name_list)
    person_select = str(input("Please type a name from the database:\n")).title()        
    if person_select in pub_name_list:
        return person_select 
    else:
        print("\nOne of your options is not in the database.\n")
        name_selector()
    

def drink_selector():
    t.print_table("drinks", drinks_menu_list)
    drink_select = str(input("Please assign a drink from the database:\n")).lower()
    if drink_select in drinks_menu_list:
        return drink_select
    else:
        print("\nOne of your options is not in the database.\n")
        drink_selector()  

def make_a_combo():
    choice1 = name_selector()
    choice2 = drink_selector() 
    return choice1 + " - " + choice2   
     

def create_an_order():
    name_add = name_input()
    drink_add = drink_input()
    round_list.append(f"{name_add} ordered {drink_add}")
    t.print_table(f"{server} is making the round", round_list)

def round_maker_loop():
    while True:
        continue_option = str(input("\nPress ENTER to continue or x to save and exit.\n"))
        if continue_option == "x":
            l.save_stuff("drinksround.csv", round_list)
            quit()
        else:
            create_an_order()

def option_1():
    t.print_table("names", pub_name_list)
    add_name_option = str(input("\nWould you like to edit this database?\n[1] Add name\n[2] Remove name\n[3] Return to menu\n"))
    if add_name_option == "1": 
        name_add()    
    elif add_name_option == "2":
        del_name()
    elif add_name_option == "3":
        wait()
    else:
        print("That's not a valid option.")
        option_1()

def option_2():
    t.print_table("drinks", drinks_menu_list)
    add_drink_option = str(input("\nWould you like to edit this database?\n[1] Add drink\n[2] Remove drink\n[3] Return to menu\n"))
    if add_drink_option == "1":
        drink_add()         
    elif add_drink_option == "2":
        del_drink()            
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
    t.print_table(f"{server} is making the round", round_list)
    create_an_order()
    round_maker_loop()

def option_8():
    t.print_table(f"{server} is making the round", round_list)
    wait() 

pub_name_list = l.load_stuff("pubnames.csv")
drinks_menu_list = l.load_stuff("drinksmenu.csv")
fav_drinks_list = l.load_stuff("favdrinks.csv")
load_round = l.load_stuff("drinksround.csv")
round_list = []


while True:           
    selection_screen()
    user_selection = user_input()
    # Organises arguments based on user input
    if user_selection == GET_NAMES:        
        option_1()
        
    elif user_selection == GET_DRINKS:        
        option_2()   
    
    elif user_selection == ASSIGN_DRINK:
        option_3()
        l.save_stuff("favdrinks.csv", fav_drinks_list)
        wait()                
                            
    elif user_selection == REMOVE_DRINK_PREF:              
        option_5()
        l.save_stuff("favdrinks.csv", fav_drinks_list)
        wait()
                
    elif user_selection == VIEW_FAV_DRINKS:          
        option_6()

    elif user_selection == CREATE_A_ROUND:
        server = str(input("Who is making the round?\n"))        
        option_7()

    elif user_selection == VIEW_ROUND:
        option_8()        
                
    elif user_selection == RUN_AWAY:
        print("We hope you enjoyed your stay.")
        exit()     
    else:
        print(f"{str(user_selection)} is not a valid command.\n")
        wait()

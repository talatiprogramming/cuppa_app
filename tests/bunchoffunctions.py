import tablecopy as t

def user_input():
    return str(input())  

def name_input():
    return str(input("Please enter a name:\n")).title()

def drink_input():
    return str(input("Please enter a drink:\n")).lower()

def round_maker():
    round_list = []
    name_add = name_input()
    drink_add = drink_input()
    round_list.append(f"{name_add} ordered {drink_add}")
    return round_list

pub_name_list = ["One", "Two", "Three"]

def name_selector():
    t.print_table("names", pub_name_list)
    person_select = str(input("Please type a name from the database:\n")).title()        
    if person_select in pub_name_list:
        return person_select 
    else:
        print("\nOne of your options is not in the database.\n")
        name_selector()



# def name_add():         
#     new_name = name_input()                                   
#     if new_name.isalpha() == False:
#         print("You can't add that to the database.\n")
#         name_add()
#     elif new_name in pub_name_list:
#         print("That entry already exists.\nPlease enter a unique name into the database.")
#         name_add()
#     else:   
#         pub_name_list.append(new_name)    
#         t.print_table("names", pub_name_list)
#         l.save_stuff("pubnames.csv", pub_name_list)
#         wait()
#defines expected commands
GET_NAMES = "1"
GET_DRINKS = "2"
ADD_NAMES = "3"
ADD_DRINKS = "4"
REMOVE_NAME = "5"
REMOVE_DRINK = "6"
ASSIGN_DRINK = "7"
VIEW_FAV_DRINKS = "8"
REMOVE_DRINK_PREF = "9"
RUN_AWAY = "0"
MENU = """Welcome to The Weary Python!
The only digital pub in town!
Please select a database to choose from:

[1]People 
[2]Drinks
[3]Add people
[4]Add drinks
[5]Remove people
[6]Remove drinks
[7]Assign favourite drinks
[8]View favourite drinks
[9]Remove favourite drink
[0]Exit\n"""

def selection_screen():
    print(MENU)

# Separate functions to ensure names don't end up in the drinks list and vice versa.
def user_input():
    return str(input())  

def names_add():
    return str(input("Please enter a name:\n")).title()

def drinks_add():
    return str(input("Please enter a drink:\n")).lower()

# Pauses the script in the middle of the while loop
def wait():
    input("Press ENTER to continue\n")

# Function that takes a string and a list and finds longest element in list
def get_table_width(title, data_set, data_set_2):
    longest = len(title) 
    spacing = 6
    for item in data_set + data_set_2:
        while len(item) > longest:
            longest = len(item)
    return longest + spacing

# Prints a table with borders based on longest element in each list provided
def print_separator(title, data_set, data_set_2):
    print("+" + "=" * get_table_width(title, data_set, data_set_2) + "+")    

def print_banner(x, y, z):
    print_separator(x, y, z)
    print(f"| {x.upper()}" + " " * (get_table_width(x, y, z) - len(f"| {x.upper()}")) + " |")
    print_separator(x, y, z)
 
def print_table(c, d, f):
    for item in d:
        print(f"| {item}" + " " * (get_table_width(c, d, f) - len(f"| {item}")) + " |")
    print_separator(c, d, f)


# Opens file and enters data into a list
def load_stuff(file):
    stuff_list = []
    try:    
        with open(file, "r") as stuff_file:        
            for line in stuff_file.readlines():
                stuff_list.append(line.strip("\n',"))
        return stuff_list
    except:
        print("Error loading file.\n")  

    
# Saves given string into a list
def save_stuff(file, stuff):
    try:
        with open(file, "a") as stuff_file:            
            stuff_file.write(stuff + "\n")
    except:
        print("Error loading file")


def delete_line(file, stuff):
    with open(file, "r") as stuff_file:
        lines = stuff_file.readlines()
    with open(file, "w") as stuff_file:
        for line in lines:
            if line.strip("\n") != stuff:
                stuff_file.write(line)

class DrinksRound:
    def __init__(self, name, drink):
        self.name = name
        self.drink = drink
    
    def assign_drink_pref(self):
        return self.name + " - " + self.drink

    def save_drink_pref(self):
        try:
            with open("favdrinks.txt", "a") as file:
                file.write(self.name + " - " + self.drink + "\n")
        except:
            print("Error saving file.\n")

    def print_drink_pref(self):
        try:
            with open("favdrinks.txt", "a") as file:
                file_list = file.readlines()
                for item in file_list:
                    print(item)
        except:
            print("Error opening file.")
    
    def del_drink_pref(self):
        stuff = self.name + " - " + self.drink
        with open("favdrinks.txt", "r") as file:
            lines = file.readlines()
        with open("favdrinks.txt", "w") as file:
            for line in lines:
                if line.strip("\n") != stuff:
                    file.write(line)


while True:
    selection_screen()
    user_selection = user_input()
    # Organises arguments based on user input
    if user_selection == GET_NAMES:
        print_banner("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
        print_table("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
        wait()              
    elif user_selection == GET_DRINKS:
        print_banner("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        print_table("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        wait()
    elif user_selection == ADD_NAMES:
        print_banner("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
        print_table("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))        
        new_name = names_add()
        if new_name.isalpha() == False:
            print("You can't add that to the database.\n")
            wait()
        elif new_name in load_stuff("pubnames.txt"):
            print("That entry already exists.\nPlease enter a unique name into the database.")
            wait()
        else:   
            save_stuff("pubnames.txt", new_name)        
            print_banner("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
            print_table("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
            wait()
    elif user_selection == ADD_DRINKS:
        print_banner("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        print_table("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        new_drink = drinks_add()
        if new_drink.isalpha() == False:
            print("You can't add that to the this database.\n")
        elif new_drink in load_stuff("drinksmenu.txt"):
            print("That entry already exists.\nPlease enter a unique drink into the database.")
            wait()
        else:
            
            save_stuff("drinksmenu.txt", new_drink)        
            print_banner("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
            print_table("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
            wait()
    elif user_selection == REMOVE_NAME:
        print_banner("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
        print_table("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))        
        name_del = names_add()        
        if name_del in load_stuff("pubnames.txt"):
            delete_line("pubnames.txt", name_del)
            print_banner("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
            print_table("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
            wait()
        else:
            print("I can't find that in the database.\n")
    elif user_selection == REMOVE_DRINK:
        print_banner("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        print_table("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        drink_del = drinks_add()
        if drink_del in load_stuff("drinksmenu.txt"):
            delete_line("drinksmenu.txt", drink_del)
            print_banner("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
            print_table("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
            wait()
        else:
            print("I can't find that in the database.")
    elif user_selection == ASSIGN_DRINK:
        print_banner("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
        print_table("names", load_stuff("pubnames.txt"), load_stuff("drinksmenu.txt"))
        person_select = str(input("Please type a name from the database:\n"))

        print_banner("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        print_table("drinks", load_stuff("drinksmenu.txt"), load_stuff("pubnames.txt"))
        drink_select = str(input("Please assign a drink from the database:\n")) 

        if person_select in load_stuff("pubnames.txt") and drink_select in load_stuff("drinksmenu.txt"):
            fav_drink = DrinksRound(person_select, drink_select)
            if fav_drink.assign_drink_pref() in load_stuff("favdrinks.txt"):            
                print("That combination has already been done. Please assign a different combination.\n") 
            else:
                fav_drink.save_drink_pref()    
        else:
            print("One of your options is not in the database.\n")
        wait()
    elif user_selection == REMOVE_DRINK_PREF:
        print_banner("fav drinks", load_stuff("favdrinks.txt"), load_stuff("pubnames.txt"))
        print_table("fav drinks", load_stuff("favdrinks.txt"), load_stuff("pubnames.txt"))
        del_name = names_add()
        del_drink = drinks_add()
        drink_pref_select = DrinksRound(del_name, del_drink)
        if drink_pref_select.assign_drink_pref in load_stuff("favdrinks.txt"):
            drink_pref_select.del_drink_pref()
        else:
            print("That is not a valid combination.")
    elif user_selection == VIEW_FAV_DRINKS:               
        print_banner("fav drinks", load_stuff("favdrinks.txt"), load_stuff("pubnames.txt"))
        print_table("fav drinks", load_stuff("favdrinks.txt"), load_stuff("pubnames.txt"))       
        wait()             
    elif user_selection == RUN_AWAY:
        print("We hope you enjoyed your stay.")
        exit()     
    else:
        print(f"{str(user_selection)} is not a valid command.\n")
        wait()







    

    
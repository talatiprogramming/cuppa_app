# Calculates the width of the largest element in a list
def get_table_width(title, data_set):
    longest = len(title) 
    spacing = 11
    for item in data_set:
        while len(item) > longest:
            longest = len(item)
    return longest + spacing

# Prints a table with borders based on longest element in each list provided
def print_separator(title, data_set): 
    print("+" + "=" * get_table_width(title, data_set) + "+")    

def print_round_table(title, data_set):
    print_separator(title, data_set)
    print(f"| {title.upper()}" + " " * (get_table_width(title, data_set) - len(f"| {title.upper()}")) + " |")
    print_separator(title, data_set)
    for item in data_set:
        print(f"| {item[0]} ordered {item[1]}" + " " * (get_table_width(title, data_set) - len(f"| {item[0]} ordered {item[1]}")) + " |")
    print_separator(title, data_set)

def print_info_table(title, data_set):
    print_separator(title, data_set)
    print(f"| {title.upper()}" + " " * (get_table_width(title, data_set) - len(f"| {title.upper()}")) + " |")
    print_separator(title, data_set)
    
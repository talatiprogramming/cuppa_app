def get_table_width(title, data_set):
    longest = len(title) 
    spacing = 2
    for item in data_set:
        while len(item) > longest:
            longest = len(item)
    return longest + spacing

# Prints a table with borders based on longest element in each list provided
def print_separator(title, data_set):
    print("+" + "=" * get_table_width(title, data_set) + "+")    

 
def print_table(title, data):
    print_separator(title, data)
    print(f"| {title.upper()}" + " " * (get_table_width(title, data) - len(f"| {title.upper()}")) + " |")
    print_separator(title, data)
    for item in data:        
        print(f"| {item}" + " " * (get_table_width(title, data) - len(f"| {item}")) + " |")
    print_separator(title, data)
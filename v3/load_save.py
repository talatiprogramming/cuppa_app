import csv

def save_stuff(file, stuff):
    try:
        with open(file, "w", newline="") as stuff_file:
            write_stuff = csv.writer(stuff_file)
            for item in stuff:
                write_stuff.writerow([item])
    except:
        print("Error saving to file")


def load_stuff(file):
    stuff_list = []
    with open(file, "r") as stuff_file:
        for line in csv.reader(stuff_file):
            for string in line:
                stuff_list.append(string)
    return stuff_list
import csv
import unittest 

def list_printer(name_add, drink_add):
    round_list = []    
    round_list.append([name_add, drink_add])
    for item in round_list:
        return f"| {item[0]} ordered {item[1]} |"

def delete_item(a_list, item):
     a_list.remove(item)
     

# def save_stuff(file, stuff):
#     try:
#         with open(file, "w", newline="") as stuff_file:
#             write_stuff = csv.writer(stuff_file)
#             for item in stuff:
#                 write_stuff.writerow([item])
#     except:
#         return "Error saving to file"

# def test_save_stuff():
#     # Arrange
#     file = "listofstuff.csv"
#     list_o_stuff = ["thing1", "thing2"]

#     # Act
#     result = save_stuff(file, list_o_stuff)

#     # Assert
#     assert result == "Error saving to file", "It broke"



def get_table_width(title, data_set, data_set_2):
    longest = len(title) 
    spacing = 2
    for item in data_set + data_set_2:
        while len(item) > longest:
            longest = len(item)
    return longest + spacing


class function_test(unittest.TestCase):   

    def test_get_table_width(self):
        # Arrange
        title = "areallylongtitle"
        list1 = ["watermelon", "cat", "dog"]
        list2 = ["blah", "blah2", "blah3"]    
        expected = 18

        # Act
        actual = get_table_width(title, list1, list2)

        # Assert
        self.assertEqual(expected, actual)

    def test_list_printer(self):
        # Arrange
        name = "bob"
        drink = "coffee"
        expected = "| bob ordered coffee |"

        # Act
        actual = list_printer(name, drink)

        # Assert
        self.assertEqual(expected, actual)
    
    def test_delete_item(self):
        # arrange
        test_list = ["apple", "banana", "pear"]
        test_string = "banana"
        expected = ["apple", "pear"]

        # act
        delete_item(test_list, test_string)

        # assert
        self.assertEqual(expected, test_list)

if __name__ == '__main__':
    unittest.main()   
    
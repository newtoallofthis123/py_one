# Author: NoobScience
# File Name: py_one_file.py
# Time: 20:52; 26-11-2022
# Place: India
# Code: https://github.com/newtoallofthis123/py_one
# License: MIT License
# Usage: Open in code editor, running the file will only print this info

# This is a python one file

# Variables
# This is an integer.
# This data type stores -n to n.
number = 12
# Decimal Data type
# No need to specify double for float
decimal = 14.845
# This is a string.
# In python, a string can store anything.
string = "Hello World!"
# A Boolean can only take two values
# True and False
# This value can be used in logical rules
boolean = True

# Some simple in built functions
# List: list()
# Converts something into a list
sample_word = "Hello World"
sample_list = list(sample_word)
# Returns ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# int()
# Converts a convertable character to an integer
int_string = "120"
string_to_int = int(int_string)
# str()
# Converts basically anything into a printable string
str_int = 120
int_to_string = str(str_int)
# float()
# Similar to float, converts a convertable integer to float
sample_float = float(120)

# Lists, Dictionaries and tuples:
# Unlike other languages like C++;
# A list in python can hold various types of data
list_example = ["Hello World", 12, True, 14.68]
# Dictonaries
# Dictonaries work with key value pair
dict_example = {
    "String": "Hello World",
    "Integer": 12,
    "Boolean": True, 
}
# Tuples
# Tuples are like lists but are non iterrable
# They are used to store data that need not be changed
tuple_example = ("Hello World", "Hi World")

if __name__ == "__main__":
    import os
    print_fashion = """
Author: NoobScience
File Name: py_one_file.py
Time: 20:52; 26-11-2022
Place: India
Code: https://github.com/newtoallofthis123/py_one
License: MIT License
Usage: Open in code editor, running the file will only print this info

This is a python one file
Open this is a code editor to read all the contents
    """
    print(print_fashion)
    print("""
    This will try to open this file in all sorts of editors. 
    If all fail, it just exits and you have to manually open it up in a code editor""")
    input("Press any key to continue...")
    try:
        os.system(f'nano {os.path.realpath(__file__)}')
    except:
        print("Unable to open in sublime, trying in VSCode")
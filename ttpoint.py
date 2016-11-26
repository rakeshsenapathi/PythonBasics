"""
__future__ module
Python 3 is supposed to be backward compatible, but some features are deprecated.
In python2 if we want to use the latest add-ons we can use __future__ module """

""" print statement in Python 2 : print "Hello World"
                    in Python 3 : print ("Hello World")
    In python 3 if we want to replace the default new line we can use end=" " to add a space instead """
print("Hello", end=" ")
print("World")
print("This works")

""" raw_input() is removed in python3, only input() works """
# x = input("Enter a number:")
# print(x + " add")

""" Python Strings:
Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([ ] and [:] ) """

str = "This is a Python String"
print(str)
print(str[0])
print(str[1:10])  # Python operators for slice([] and [:])

""" Python Lists """
list = ["Groceries", 100, "Mobile Phone", ["Earphones", "Cricket Bat"]]
print(list[3][0])



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

""" Python Tuples: They are similar to lists but have the following differences
    1) Tuples are enclosed by ( ) 
    2) We cannot update the tuples unlike lists, so they can be called as read-only lists"""
tuple = ("Groceries", 100, "Mobile Phone", ("Earphones", "Cricket Bat"))
print(tuple)

""" Python dictionary: There are similar to hash tables i.e key and value pairs """
my_dictionary = {
 	               1 : "Number 1",
 	               2 : "Number 2",
 	               "three" : 3
                }
print(my_dictionary["three"])

""" Data type conversions """
#int 
x = int(17.2)
print(x)

""" Some of Python Arithmetic Operators """

#Division
d = 4/3
print(d) #The output can result a float point, for this floor division can be used

#Floor Division
f = 4//3
print(f) #returns floor value

#Exponent
e = 4**2
print(e)

""" Identity Operator: Python built-in function id() returns a unique integer as identity of object.
    *** Refer to the pythons memory and execution model :
    Link: https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/ """

a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is b ):
   print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print ("Line 3 - a and b have same identity")
else:
   print ("Line 3 - a and b do not have same identity")

b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is not b ):
   print ("Line 5 - a and b do not have same identity")
else:
   print ("Line 5 - a and b have same identity")
# In python here 20 object is created and assigned to variable and when it changes to 20 the id() value also changes. It's execution varies from others.

""" Loop Statements:
    Python supports the following Control Statements 1) break 2) continue 3) pass """
#Continue statement
for letter in 'Python':
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

"""Pass statement: It is a null operation, it does execute anything but is rather used to acheive syntactical correctness. It simple acts as a 
place holder for the methods et cetera, which are not yet there"""

for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")

"""Iterator is an object which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation.
In Python iterator object implements two methods : iter() and next()"""

the_list=[1,2,3,4]
it = iter(the_list) # this builds an iterator object
#print (next(it)) #prints next available element in iterator

for each_element in it:
	print (each_element, end= " ") #end is used to avoid default new line with each iteration


    






a = 10
b = 10
c = 20
d = 10

if(id(a) == id(b)):
    print("This is true")

print("First line", end = "    ")
print("Second Line")

mylist = []
mylist = ["Rakesh","Senapathi"]
for each_it in mylist:
    print(each_it)

mytuple = ( "Lorium",48,"Ipsum" , ("Lorium---Ipsum", "Lorium") )


print(mytuple)


#Test on tuples
t = (1,2,3,4)
t2 = t+t
print(t2)

# Converting a list into a tuple
conv_tuple = tuple(mylist)

print(conv_tuple)

my_dictionary = {
    "Key" : "value"
    }

print(my_dictionary["Key"])

alt_dict = my_dictionary.copy()
print(alt_dict)

#clear() is used to clear the contents of the dictionary
""" To overwrite the contents of a dictionary, we can use update() method """

# A set is a dictionary with no values, it just has unique keys

set1 = {1,2,3}
set2 = {1,2,3,4,5}

set3 = set1 & set2
if(set3 == set1):
    print("Set1 and Set3 are the same!")

set4 = set1 | set2
if(set4 == set2):
    print("Set2 and Set4 are the same as well")

















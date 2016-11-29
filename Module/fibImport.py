# Import various modules
import fib
import os
number = 300
result = fib.fib_gen(number)
print(result)
fib.main()  # know from where is executed, here it is executed from fib which is imported

""" Output the result to a text file """
file = open("fibseries.txt", "w")
for each_item in result:
    file.write(str(each_item) + " ")
file.close()

""" Current location of the directory """
current_location = os.getcwd()
print(current_location)

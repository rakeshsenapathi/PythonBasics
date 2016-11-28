""" Random number functions: Random ni are needed for various scenarios """
import random
# 1) choice : Randomly generated from a list or tuple

list = ['google','facebook','youtube','gmail','twitter','instagram','snapchat']
print(random.choice(list))

#) 2) selectively random : A randomly selected element from range(start, stop, step)

print(random.randrange(1,100,5))

#) 3) random() : A random float r, such that 0 is less than or equal to r and r is less than 1

print(random.random())

#) 4) Shuffle():
random.shuffle(list) #It returns none
print("Shuffled list:",list)

""" String formatting operator:This operator is unique to strings and makes up for the pack of having functions from C's printf() family."""

print("this is %s of number: %d" % ('test',21))

""" Date and Time: Python """
import time
present_time = time.localtime(time.time())
print(present_time)
#To get formatted time we can use asctime() method
fCurrent_time = time.asctime(present_time) #Formatted current time
print(fCurrent_time)

#Get calender of a month
import calendar
print(calendar.month(2016,12))
# miscellaneous time methods
print(time.clock()) #returns current CPU time as float points

time.sleep(2) #suspends the thread for a specific time period
print("Two seconds done!")

# miscellaneous calendar methods

print(calendar.isleap(2016)) #returns true or false
print(calendar.leapdays(2012,2016)) 
print(calendar.monthcalendar(2016,5))

""" Other interesting modules are 
1)The datetime Module
2)The pytz Module
3)The dateutil Module """


""" Functions : In python arguments are passed by reference 
    There are 4 types of arrguments
    1) Regular Arguments
    2) Keyword Arguments
    3) Default Arguments 
    4) Variable-length Arguments """

#Anonymous Function : You can use the lambda keyword to create small anonymous functions.

sum = lambda arg1,arg2 : arg1+arg2 #Function is defined here
print("Sum is", sum(10,10))

""" Local vs Global Variables """

total = 0 # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )


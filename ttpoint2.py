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

print(list*2)
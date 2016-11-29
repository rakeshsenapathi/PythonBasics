# Module for Fibonacci numbers


def fib_gen(number):
    result = []  # Initialise an empty list
    a, b = 0, 1
    while (b < number):
        result.append(b)
        a, b = b, a + b
    return result

def main():
	print("We are in", __name__)

if(__name__ == '__main__'):
	print("This is executed in __main__")

def isPrime(number):
	value = 1
	i = number // 2
	for each_iter in range(2,i+1):
		if( number % each_iter == 0):
			value = 0
		else:
			continue
	return value

if(isPrime(45)):
	print("Is prime")
else:
	print("Not a prime")

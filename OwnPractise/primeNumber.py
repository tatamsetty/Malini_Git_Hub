num = 11
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
    isItPrime = True
    for i in range(2, int(num/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
        if (num % i) == 0:
            isItPrime = False
            break
    if isItPrime == False:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
else:
	print(num, "is not a prime number")

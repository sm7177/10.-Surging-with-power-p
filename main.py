def checkPowerof8(n):
	
	i = 0
	l = 1
	
	while (i <= 63):
		l <<= i

		if (l == n):
			return True

		i += 3
		l = 1

	return False

if __name__ == '__main__':
	
	n =int(input("Enter a number:"))
	if (checkPowerof8(n)):
		print("It is a power of 8")
	else:
		print("It is not a power of 8   ")

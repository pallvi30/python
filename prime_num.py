def is_prime(n):
	for i in range (2,n):
		if n%i==0:
			return False
	return True
n=input("enter the number")
for x in range (2, int(n)):
    if is_prime(x):
        print(x, "is prime number")
    else:
        print(x, "is not prime number")
    
    

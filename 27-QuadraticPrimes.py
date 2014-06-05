import math
def is_prime(n):
    if n <2:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def countPrimes(a,b):
	n=0
	#calc = n*n + a*n + b
#	print a,b, calc
	while is_prime(n*n + a*n + b):
		n+=1
		#calc = n**2 + a*n + b
		#print calc
	return n

#print countPrimes(1,41)
#print countPrimes(-79,1601)

besta=0
bestb=0
maxCount=0
for a in range(-1000,1000):
	for b in range(a,1000):
		c = countPrimes(a,b)
		if c > maxCount:
			maxCount = c
			besta = a
			bestb = b
			print a,b,c

print besta*bestb

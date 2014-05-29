import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

count=6
num = 13
while count < 10001:
	num+=1
	if is_prime(num):
		count +=1
	print count, num

print num

i = 1
sums = 0
sumSquares = 0
while i <= 100:
	print i
	sums += i
	sumSquares +=i**2
	i+=1

sumsSq = sums**2
print sumsSq, sumSquares, sumsSq - sumSquares

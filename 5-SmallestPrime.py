def evenDivisible(number):
    i = 2
    while i <= 20:
        if number % i !=0:
            #print "{a} not divisble by {b}".format(a=number, b=i)
            return False
        #print "{a} divisble by {b}".format(a=number, b=i)
        i+=1
    return True

counter=2520
while evenDivisible(counter) == False:
	counter+=20
print counter

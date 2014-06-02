
def isPalindrome(num):
	strNum = str(num)
	index = 0
	maxi = len(strNum)-1
	while index <= maxi/2:
		#print strNum[index], strNum[maxi-index]
		if strNum[index] != strNum[maxi-index]:
			return False
		index +=1
	return True

print isPalindrome(82345)
print isPalindrome(123421)
print isPalindrome(12321)
print isPalindrome(123321) 

maxProd = 0

for a in range(100,999):
	for b in range (a,999):
		prod = a*b
		if (isPalindrome(prod)):
			maxProd = max(maxProd,prod)
			print maxProd

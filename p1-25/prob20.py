import math

a= str(math.factorial(100))

b=list(a)

sum = 0

for x in xrange(0,len(b)-1):
	sum = sum + int(b[x])

print sum


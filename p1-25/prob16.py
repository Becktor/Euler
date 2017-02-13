
numb = 2**1000
def sum_of():
	sum=0
	a=list(str(numb))
	print len(a)
	for x in xrange(0,len(a)):
		sum = sum+int(a[x])
	print sum

sum_of()
	

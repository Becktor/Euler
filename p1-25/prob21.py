list_one = []
list_two = []
temp_sum = 0
temp_two_sum = 0



for x in xrange(1,10000):
	temp_sum = 0
	temp_two_sum=0

	for n in xrange(1,x):
		if x % n==0:
			temp_sum = temp_sum + n

	for k in xrange(1,temp_sum):
		if temp_sum%k==0:
			temp_two_sum = temp_two_sum + k
	
	if temp_two_sum == x and temp_sum !=temp_two_sum:
		list_two.append(temp_two_sum)				

print list_two
sumss=0

for x in xrange(0	,len(list_two)):
	sumss = int(list_two[x])+sumss
	print sumss

print sumss	
	

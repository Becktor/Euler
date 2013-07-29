
one_to_nine=["one","two","three","four","five","six","seven","eight" ,"nine"]

eleven_to_nineteen=["ten","eleven","twelve","thirteen", "fourteen","fifteen",
					"sixteen","seventeen","eighteen", "nineteen",]

ten_to_ninety=["twenty", "thirty", "forty", "fifty", "sixty",
					 "seventy", "eigthy", "ninety"]
hundred = -2
tens = -3
teens = 0
ones = 0
ten_ones = 0
numbs=[]

for x in xrange(0,1001):

	if ones >8:
		ones=0
	if x<9:
		numbs.append(one_to_nine[ones])
		ones = ones +1

	if (x%10==0):
		tens = tens + 1
	if teens >9:
		teens = 0

	if tens >7:
		tens=0	

	if x >9 and x<19:
		numbs.append(eleven_to_nineteen[teens])
		teens = teens +1

	if x>19	 and x<100:

		if (x%10==0):
			print tens
			numbs.append(ten_to_ninety[tens])
		else:
			if ten_ones == 9:
				ten_ones = 0
			numbs.append("%s%s"%(ten_to_ninety[tens],one_to_nine[ten_ones]))
			ten_ones = ten_ones + 1

	if x>100 and x<1000:
		
		if (x%10==0):
			numbs.append("%shundredand%s"%(one_to_nine[hundred],ten_to_ninety[tens]))
		
		else:
			if x%100 > 9 and x%100 < 19:
				print "yo"
				if ten_ones == 9:
					ten_ones = 0
				numbs.append("%shundredand%s%s"%(one_to_nine[hundred],ten_to_ninety[tens],eleven_to_nineteen[ten_ones]))
				ten_ones = ten_ones + 1
			else:
				if ten_ones == 9:
					ten_ones = 0

				numbs.append("%shundredand%s%s"%(one_to_nine[hundred],ten_to_ninety[tens],one_to_nine[ten_ones]))
				ten_ones = ten_ones + 1

	if x==1000:
		numbs.append("onethousand")		

	if (x%100==0):
		hundred = hundred +1
sum = 0
for x in xrange(0,999):
	print numbs[x]
	sum = sum + len(numbs[x])
print sum	






			
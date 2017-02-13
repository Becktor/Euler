zero = "zero"
one = "one"
two	= "two"
three ="three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine ="nine"
ten = "ten"
eleven = "eleven"
twelve = "twelve"
thirteen = "thirteen"
fourteen = "fourteen"
fifteen = "fifteen"
sixteen = "sixteen"
seventeen="seventeen"
eightteen = "eightteen"
nineteen = "nineteen"
twenty = "twenty"
thirty = "thirty"
fourty ="fourty"
fifty = "fifty"
sixty = "sixty"
seventy = "seventy"
eigthy ="eigthy"
ninety = "ninety"
hundred ="hundred"

one_to_nine=["one","two","three","four","five","six","seven","eight" ,"nine"]

eleven_to_nineteen=["eleven","twelve","thirteen", "fourteen","fifteen",
					"sixteen","seventeen","eightteen", "nineteen"]

ten_to_ninety=["ten","twenty", "thirty", "fourty", "fifty", "sixty",
					 "seventy", "eigthy", "ninety"]
hundred = -2
tens = -2
ones = 0
ten_ones = 0
numbs=[]

for x in xrange(0,1001):

	if ones >8:
		ones=0
	if x<9:
		print one_to_nine[ones]
		numbs.append(one_to_nine[ones])
		ones = ones +1

	if (x%10==0):
		tens = tens + 1


	if tens >8:
		tens=0	

	if x >9 and x<19:
		if (x%10==0):
			print ten_to_ninety[tens]
			numbs.append(ten_to_ninety[tens])
		print eleven_to_nineteen[ones]
		numbs.append(eleven_to_nineteen[ones])
		ones = ones +1

	if x>19 and x<100:

		if (x%10==0):
			print ten_to_ninety[tens]
			numbs.append(ten_to_ninety[tens])
		else:
			if ten_ones == 9:
				ten_ones = 0
			print "%s-%s"%(ten_to_ninety[tens],one_to_nine[ten_ones])
			numbs.append("%s-%s"%(ten_to_ninety[tens],one_to_nine[ten_ones]))
			ten_ones = ten_ones + 1

	if x>100 and x<1000:
		if (x%10==0):
			print "%s hundred and %s"%(one_to_nine[hundred],ten_to_ninety[tens])
			numbs.append("%s hundred and %s"%(one_to_nine[hundred],ten_to_ninety[tens]))
		else:
			if ten_ones == 9:
				ten_ones = 0

			print "%s hundred and %s-%s"%(one_to_nine[hundred],ten_to_ninety[tens],one_to_nine[ten_ones])
			numbs.append("%s hundred and %s-%s"%(one_to_nine[hundred],ten_to_ninety[tens],one_to_nine[ten_ones]))
			ten_ones = ten_ones + 1
	if x==1000:
		print "one thousand"
		numbs.append("one thousand")		

	print numbs
	print len(numbs)
	if (x%100==0):
		hundred = hundred +1







			
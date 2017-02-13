from math import sqrt
 
def d(n):
	s = 1
	t = sqrt(n)
	for i in range(2, int(t)+1):
  		if n % i == 0: s += i + n / i
	if t == int(t): s -= t

	return s

s = 0
abund = set()
for n in range(1, 20162):
	if d(n) > n:
		abund.add(n)
	if any((n-a in abund) for a in abund):
		pass
	else:
		s += n
 
print "ANSWER IS HEAR! ", s
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_century = 36525
sundays=0

def sund_count():
	day_cntr=1
	week_cntr=1
	month_cntr=0
	year_cntr = 0
	leap = False
	years = 1
	lyears = 0
	while years < 100:

		pass
		if years%4==0 and years!= 0:
			#global leap
			#print "het"
			leap = True
		else:
			leap = False

		if day_cntr >= months[month_cntr]:
			if 	leap and months[month_cntr]==months[1] and day_cntr==28:
				day_cntr = day_cntr +1
			else:
				day_cntr=1
				month_cntr = month_cntr + 1

		if year_cntr > 365:
			if leap and year_cntr==365:
				year_cntr = year_cntr + 1
				#print year_cntr
			else:
				if leap:
					print years
					lyears = lyears +1
				year_cntr = 1
				years = years +1
				


		if week_cntr > 6:
			week_cntr= 0
		if month_cntr > 11	:
			month_cntr= 0



		if day_cntr == 1 and week_cntr==6:
			global sundays
			sundays = sundays + 1

		
		
		year_cntr = year_cntr + 1
		day_cntr = day_cntr + 1
		week_cntr = week_cntr + 1

	print lyears, years

sund_count()

print sundays


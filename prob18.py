#!/usr/bin/env python
 
import time

def cntr(row):
	for i,j in [(i,j) for i in range(len(rows)-2,-1,-1) for j in range(i+1)]:
	    rows[i][j] +=  max([rows[i+1][j],rows[i+1][j+1]])

# read file to rows
def read(file):
	for row in FILE: rows.append([int(i) for i in row.split(" ")])






rows = []
FILE = open("18.data", "r")
 
start = time.time()
read(FILE)
cntr(rows)
elapsed = time.time() - start
 
print "%s found in the time %s seconds" % (rows[0][0],elapsed)

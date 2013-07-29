


FILE = open("names.txt", "r")
names = FILE.readline().replace('\"','').split(',')
names.sort()

total = 0
for x in xrange(0,len(names)):
    name=list(names[x])
    name_len=0
    for n in xrange(0,len(name)):
        name_len = name_len + (ord(name[n])-64)

    total = total + (x+1)*name_len

print total
in_file = open('names.txt', 'r')
names = in_file.readline().replace('\"','').split(',')
names.sort()
worth = lambda idx, name: idx * sum([ord(x) - ord('A') + 1 for x in name])
print sum([worth(idx+1, name) for (idx, name) in enumerate(names)])
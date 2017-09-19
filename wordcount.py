import sys
from collections import OrderedDict

# This script is used for my personal reports

fo = open(sys.argv[1], 'r')
count = int(sys.argv[2])
tel = {}

with fo as f:
	for line in f:
		for word in line.split():
			if word not in tel:
				tel[word] = 1
			else:
				tel[word] = tel[word] + 1

# def wordCount(number):

def wordCount(file, input):
	tel_sorted_by_value = OrderedDict(sorted(file.items(), key = lambda x: x[1], reverse=True))
	for x in xrange(input):
		print tel_sorted_by_value.popitem(last=False)

if  __name__ == "__main__":
	print "This is the name of the script", sys.argv[0]
	print "This is the name of the file", sys.argv[1]
	print "How many words to view?", sys.argv[2]
	print tel
	wordCount(tel, count)
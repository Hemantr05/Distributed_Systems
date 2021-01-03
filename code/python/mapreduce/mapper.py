#!/usr/bin/env python

import sys

#store = {}

for line in sys.stdin:

	line = line.strip()

	words = line.split()

	for word in words:

#		store[word] = "1"
		print("%s\t%s"%(word,1))
#print(store)

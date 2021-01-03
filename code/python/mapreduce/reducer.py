#!/usr/bin/env python

import sys

current = None
word_count = 0
word = None

for line in sys.stdin:
	line = line.strip()

	word, count = line.split('\t', 1)

	try:
		count = int(count)
	except ValueError:
		continue

	if current == word:
		word_count += count

	else:
		if word:
			print("%s\t%s" % (word, word_count))
		word_count = count
		current = word

if current == word:
	print("%s\t%s"%(current, word_count))

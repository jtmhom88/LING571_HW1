#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import nltk
from collections import defaultdict
import pprint

# Dictionary to hold all POS tags and tokens
d = defaultdict(list)
pp = pprint.PrettyPrinter(indent=4)

i = 0
for line in open('inputfile.txt','r'):
	i += 1
	#if i <= 4:
	if True:
		# Take sentence and return tokens
		text = nltk.word_tokenize(line)
		#print text , '\n'
		# POS tag all the tokens
		posl = nltk.pos_tag(text)
		#print posl
		# For all elements of the pos list, stuff in dictionary
		for elem in posl:
			d[elem[1]].append(elem[0])
			#pp.pprint(d)
		pass
	pass
pp.pprint(d)
print "Owari\n"



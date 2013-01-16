#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import nltk

i = 0
for line in open('inputfile.txt','r'):
	i += 1
	if i == 1:
		text = nltk.word_tokenize(line)
		print text , '\n'
		poslist = nltk.pos_tag(text)
		print nltk.pos_tag(text) , '\n'
		break
		pass
	pass



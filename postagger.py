#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import nltk

outfile = open('poslist.txt','w')

i = 0
for line in open('inputfile.txt','r'):
	i += 1
	#if i <= 4:
	if True:
		# Tokenize the sentence
		text = nltk.word_tokenize(line)
		#print text , '\n'
		# Pos tage the tokens
		poslist = nltk.pos_tag(text)
		posl = nltk.pos_tag(text)
		print posl
		outfile.write(str(posl) + '\n')
		pass
	pass

print "Owari\n"



#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""
from __future__ import print_function
from collections import defaultdict
import pprint
import ast


__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

# Dictionary to hold all POS tags and tokens
d = defaultdict(list)
pp = pprint.PrettyPrinter(indent=4)
	
i = 0
for line in open('poslist.txt','r'):
	i += 1
	#if i <= 4:
	if True:
		# read in file of Pos tagged sentences
		posl = ast.literal_eval(line)
		#print posl
		# For all elements of the pos list, stuff in dictionary
		for elem in posl:
			d[elem[1]].append(elem[0])
#			pp.pprint(d)
		pass
	pass

pp.pprint(d)
print('\n')

words = []

# Iterate dictionary
for k, v in d.iteritems():
	print ( k,' -> ', end='')
	# Iterate the lists
	for val in v:
		print (val, '| ', end='')
#		print ('\'',val,'\'', '| ', end='')
#		if not (val in words):
	#		words.append(val)
#			print (val, '| ', end='')
#			pass
	print ('\n')
	pass
#print "Owari\n"



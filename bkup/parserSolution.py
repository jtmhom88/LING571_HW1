#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import nltk

grammar1 = nltk.parse_cfg(
  """
	S -> NP VP
	S -> VP

	NP -> NNS
	NNS -> 'dogs'

	VP -> VBP
	VBP -> 'bark'
  """)

print grammar1 , '\n'

#parser = nltk.RecursiveDescentParser(grammar1)
parser = nltk.parse.EarleyChartParser(grammar1)

i = 0
for line in open('inputfile.txt','r'):
  i += 1
  pass
  if i == 1:
    sent = "dogs bark".split()
    #sent = line.split()
    print sent , '\n'
    pp = parser.parse(sent)
    print pp, '\n'
    break
    pass
  



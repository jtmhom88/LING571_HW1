#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import nltk
from nltk.tokenize import wordpunct_tokenize 

gstring = open('solutiongrammar.cfg', 'r').read()
grammar1 = nltk.parse_cfg(gstring)
                          
#grammar1 = nltk.parse_cfg(
#"""
#	S -> NP VP PUNC
#
#  NP -> N | DT N | DT N PP
#  N -> 'Work' | 'work' | 'growth' | 'muscles'
#
#  DT -> 'the'
#  
#  VP -> V | V NP | V NP PP
#  V -> 'accelerates'
#	#VBZ -> 'accelerates'
#	
#	PP -> IN NP
#	IN -> 'of'
#	
#	PUNC -> '.'
#"""
#)

print grammar1 , '\n'

#parser = nltk.RecursiveDescentParser(grammar1)
parser = nltk.parse.EarleyChartParser(grammar1)

i = 0
for line in open('inputfile.txt','r'):
  i += 1
  pass
  if i <= 6:
    #sent = "dogs bark".split()
    #sent = line.split()
    #sent = wordpunct_tokenize(line)
    #line = "An average adult male is made up of 45% skeletal muscle."
    #line = "A male and a female accelerates and a male accelerates."
    #line = "An average adult male is made up of 45% skeletal muscle and an average adult female is made up of 35% skeletal muscle."
    #line = "Old people are at risk for arthritis."
    sent = wordpunct_tokenize(line)
    print sent , '\n'
    pp = parser.parse(sent)
    print pp, '\n'
    #break
    pass
  



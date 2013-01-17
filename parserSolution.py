#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import nltk
from nltk.tokenize import wordpunct_tokenize 
from sys import argv

script, inlineno = argv
print "Line requested: ", inlineno

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

#print grammar1 , '\n'

#parser = nltk.RecursiveDescentParser(grammar1)
parser = nltk.parse.EarleyChartParser(grammar1)

i = 0
for line in open('inputfile.txt','r'):
  i += 1
  pass
  if i == int(inlineno):
    print line
    #sent = "dogs bark".split()
    #sent = line.split()
    #sent = wordpunct_tokenize(line)
    #line = "An average adult male is made up of 45% skeletal muscle."
    #line = "A male and a female accelerates and a male accelerates."
    #line = "An average adult male is made up of 45% skeletal muscle and an average adult female is made up of 35% skeletal muscle."
    #line = "Old people are at risk for arthritis."
    #line = "The action is determined by the origin and insertion locations."
    #line = "A pain in the abdomen is appendicitis."
    #line  = "The motor system  is responsible."
    #line = "Do you have pain in the muscles on the side of the face?"
    #line = "Scientists finally realized that DNA controls heredity."
    #line = "A pain in the abdomen lasting more than a week could be appendicitis."
    #line = "There is much research on the growth of muscles."
    #line = "Few people privy to the research ."
    sent = wordpunct_tokenize(line)
    print sent , '\n'
    #pp = parser.parse(sent)
    pp = parser.nbest_parse(sent)
    j = 0
    for p in pp:
      j += 1
      print "Parse: ", j, "\n", p, "\n"
      #break
    pass
    print "Number of parses: %d" % j
  



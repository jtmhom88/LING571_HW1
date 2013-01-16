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
   NP -> Det N | Det N PP | "I"
   VP -> V | V NP | V NP PP
   PP -> P NP
   V -> "saw" | "ate"
   Det -> "a" | "the"
   N -> "man" | "dog" |"telescope" | "park"
   P -> "in" | "under" | "with"
   """)

print grammar1 , '\n'

#parser = nltk.RecursiveDescentParser(grammar1)
parser = nltk.parse.EarleyChartParser(grammar1)

sent = "the dog saw a man in the park".split()

print sent , '\n'

print parser.parse(sent) , '\n'


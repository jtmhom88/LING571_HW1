#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Take in as an argument the type of parser you want.
Options:
1. rd = rd_parser = nltk.RecursiveDescentParser(grammar1)
2. sr = sr_parse = nltk.ShiftReduceParser(grammar1)
3. ec = ec_parser = nltk.parse.EarleyChartParser(grammar1)
4. td = td_parser = nltk.parse.TopDownChartParser(grammar1)
5. bu = bu_parser = nltk.parse.BottomUpChartParser(grammar1)
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

import sys
import argparse
from datetime import datetime
import nltk
from nltk.tokenize import wordpunct_tokenize 
from nltk.parse import EarleyChartParser, TopDownChartParser, BottomUpChartParser


def Solution_parse(args):
  try:
    print "Parser option: %s " % args.parseOption
    gstring = open('solutiongrammar.cfg', 'r').read()
    grammar1 = nltk.parse_cfg(gstring)
    #print grammar1 , '\n'
    
    if (args.parseOption == 'rd'):
      parser = nltk.RecursiveDescentParser(grammar1)
    elif(args.parseOption == 'sr'):
      parser = nltk.ShiftReduceParser(grammar1)
    elif(args.parseOption == 'ec'):
      parser = nltk.parse.EarleyChartParser(grammar1)
    elif(args.parseOption == 'td'):
      parser = nltk.parse.TopDownChartParser(grammar1)
    elif(args.parseOption == 'bu'):
      parser = nltk.parse.BottomUpChartParser(grammar1)
    else:
      raise Exception("Unknown parseOption: %s" % args.parseOption)

    i = 0
    for line in open('inputfile.txt','r'):
      i += 1
      pass
      if i == 1:
        print line
        sent = wordpunct_tokenize(line)
        print sent , '\n'
        pp = parser.parse(sent)
        print pp, '\n'
        pass

  except Exception, err:
    sys.stderr.write('ERROR: %s\n' % str(err))
    raise
  finally:
    pass
  

###############################

def main():
  try:
    print 'Started ParserSolution run at: {0}'.format(datetime.now())
    parser = argparse.ArgumentParser(description='Execute Yahoo_API Run', formatter_class=argparse.RawDescriptionHelpFormatter)
    args = parser.add_argument('parseOption', help='parseOption')
    args = parser.parse_args()
    print args
    Solution_parse(args)
  except Exception, ex:
    print 'Exception occurred: {0}'.format(ex)
    sys.exit(-1)
  finally:
    print 'Finished run at: {0}'.format(str(datetime.now()))

  exit()
  pass

### MAIN
if __name__ == '__main__':
  main()
  

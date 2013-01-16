#!/usr/bin/python
#

"""This script fulfills HW1 LING571.
Uses the EarleyChartParser.
"""

__author__ = 'johnnyhom@gmail.com (Johnny Hom)'

from collections import defaultdict
import pprint

#a = [('Work', 'NNP'), ('accelerates', 'VBZ'), ('the', 'DT'), ('growth', 'NN'), ('of', 'IN'), ('muscles', 'NNS'), ('.', '.')] 

a = [('Work', 'NNP'), ('accelerates', 'VBZ'), ('horse', 'NNP'), ('the', 'DT')] 

d = defaultdict(list)

pp = pprint.PrettyPrinter(indent=4)

for i in a:
    d[i[1]].append(i[0])
    pp.pprint(d)
    


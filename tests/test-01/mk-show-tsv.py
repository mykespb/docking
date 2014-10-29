#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# mk-show-tvs.py
# (C) Mikhail (myke) Kolodin, 2014
#
# read data from latest run of docker in dump.tsv

import csv
import datetime
from matplotlib.dates import strpdate2num
import numpy as np
import matplotlib.pyplot as plt
from pylab import figure, show
incvs = 'dump.tsv'

def main():

    print "here are statistic data"

    with open('dump.tsv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            print ', '.join(row)



    return 0

if __name__ == '__main__':
    main()



#~ import csv
#~
#~ def main():
#~
    #~ print "here are statistic data"
#~
    #~ with open('dump.tsv', 'rb') as csvfile:
        #~ spamreader = csv.reader(csvfile, delimiter='\t')
        #~ for row in spamreader:
            #~ print ', '.join(row)
            #~
            #~
            #~
    #~ return 0
#~
#~ if __name__ == '__main__':
    #~ main()
#~

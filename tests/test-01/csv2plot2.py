#!/usr/bin/env python2
# coding: utf-8

# 2014-08-17 2014-10-29 2.1
# csv2plot2.py
# Mikhail (myke) Kolodin

# read csv file with programs code amounts data and make plots on progress

import datetime
from matplotlib.dates import strpdate2num
import numpy as np
import matplotlib.pyplot as plt
from pylab import figure, show

incvs = 'dump.tsv'
tcsv  = 'dump.temp'

def main():
    """ dispatcher """

    xdata = []
    ydata = []
    with open (incvs, 'rb') as fin, open (tcsv, 'wb') as touf:
        print >>touf, "%s,%s,%s,%s" % ("dt", "cont", "cpu", "virtmem")
        for row in fin:
            r = row.split()
            print >>touf, "%s,%s,%s,%s" % (r[0] + ' ' + r[1], r[2][4:], r[3], r[4])
            print "%s,%s,%s,%s" % (r[0] + ' ' + r[1], r[2][4:], r[3], r[4])

    plt.plotfile (tcsv, cols = ("cont", "cpu"))
    plt.xlabel(u"число контейнеров")
#    plt.xlabel("number of containers")
    plt.ylabel(u"использование ЦПУ")
#    plt.ylabel("CPU usage")
    plt.ylim(0, 100)
    plt.grid()
    plt.xticks(rotation=45)
#    plt.xticks(rotation='vertical')
    plt.savefig ("docker-cpu.png", bbox_inches='tight')

    plt.plotfile (tcsv, cols = ("cont", "virtmem"))
#    plt.xlabel("number of containers")
    plt.xlabel(u"число контейнеров")
#    plt.ylabel("virtual memory")
    plt.ylabel(u"виртуальная память")
    plt.ylim(0, 100)
    plt.grid()
    plt.xticks(rotation=45)
#    plt.xticks(rotation='vertical')
    plt.savefig ("docker-virtmem.png", bbox_inches='tight')

    #~ plt.show()
    return 0

if __name__ == '__main__':
    main()


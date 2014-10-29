#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# mk-dockter-1-2.py 2014-10-30 1.1.1-3
# (c) Mikhail (myke) Kolodin, 2014
# test own tests acc to ofic docs - OK

import time
import docker
import psutil
import datetime
import os

from pprint import pprint as pp

import sqlite3
conn = sqlite3.connect(':memory:')
cur  = conn.cursor()
cur.execute ("create table recs (dt, nomo, cpu, virt)")
conn.commit()

def crecont (dc, name="noname"):
    """ create container """
    print "create container [%s], " % name,
    try:
        ctr = dc.create_container('ubuntu:14.04', name=name)
        print "created container, "

        print "starting, ",
        dc.start(ctr)
        print "started, "

        #~ pp(dc.info())
        #~ pp(dc.inspect_container(ctr))
        #~ print psutil.cpu_percent(percpu=False),
        #~ print psutil.cpu_percent(percpu=True)

        #~ print "virtual memory used %: ", psutil.virtual_memory().percent
        #~ print "swap memory used %: ", psutil.swap_memory().percent

        try:
            dt = datetime.datetime.now()
            cpu = psutil.cpu_percent(percpu=False)
            virt = psutil.virtual_memory().percent
            print "db: ", dt, cpu, virt
            cur.execute ("insert into recs values (?,?,?,?)", (dt, name, cpu, virt))
            conn.commit()
        except:
            print "crecont database error"

        return ctr
    except:
        print "error: crecont"

def delcont (dc, ctr, name="noname"):
    """ delete (stop & remove) container """
    print "killing container [%s], " % name,
    try:
        dc.stop(ctr)
        dc.remove_container(ctr)
        print "killed, "
    except:
        print "error: delcont"

def procctr (dc, name="noname"):
    """ process container """
    print "process ctr [%s]: " % name
    try:
        ctr = crecont (dc, name)
        print dc.inspect_container (ctr)
        delcont (dc, ctr, name)
    except:
        print "finished procctr"
    print "finish ctr [%s]: " % name

def dbdump():
    with open('dump.tsv', 'w') as f:
        cur.execute ("select * from recs order by dt")
        for row in cur:
            f.write('%s\t%s\t%s\t%s\n' % row)

def main1():
    try:
        print "making client, ",
        dc = docker.Client(base_url='unix://var/run/docker.sock', version='1.14', timeout=10)
        print "client ready, "

        print "version: ", dc.version()

#        procctr (dc, "mycont-3")

        print "run all tests"
#        names = "eins zwei drei vier funf sechs sieben acht neun zehn".split()
#        names = "eins zwei drei".split()
#        names = ['ctr-'+str(n) for n in xrange(1000)]
        names = ['ctr-'+str(n) for n in xrange(100)]

        print "names: ", names

        #~ for name in names:
#~ #            procctr (dc, "%s" % name)
            #~ ctr = crecont (dc, name=name)
            #~ delcont (dc, ctr, name)

        ctrs = []

        try:
            for name in names:
                ctrs += [[name, crecont (dc, name=name)]]

            for ctr in ctrs:
                delcont (dc, ctr[1], ctr[0])

        except:
            print "bad names processing"

        print "all done"

    except:
        print "bad docker"

    dbdump()

    with open('dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()

    return 0

if __name__ == '__main__':
    main1()

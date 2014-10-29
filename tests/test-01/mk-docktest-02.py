#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# mk-docktest-01.py 2014-10-30 1.1
# (C) Mikhail (myke) Kolodin, 2014
# test method from (OK):
# http://blog.bordage.pro/avoid-docker-py/

import time
import docker
import psutil

from subprocess import Popen, PIPE

def kill_and_remove(ctr_name):
    for action in ('kill', 'rm'):
        p = Popen('docker %s %s' % (action, ctr_name), shell=True,
                  stdout=PIPE, stderr=PIPE)
        if p.wait() != 0:
            raise RuntimeError(p.stderr.read())


def execute(code, ctr_name="any_name"):
#    ctr_name = 'ctr_3'
    p = Popen(['timeout', '-s', 'SIGKILL', '2',
               'docker', 'run', '--rm', '--name', ctr_name,
               'ubuntu:14.04', 'python3', '-c', code],
              stdout=PIPE)
    out = p.stdout.read()

    if p.wait() == -9:  # Happens on timeout
        # We have to kill the container since it still runs
        # detached from Popen and we need to remove it after because
        # --rm is not working on killed containers
        kill_and_remove(ctr_name)

    return out

def launch(code, ctr_name="any_name"):
#    ctr_name = 'ctr_3'
    p = Popen(['timeout', '-s', 'SIGKILL', '2',
               'docker', 'run', '--rm', '--name', ctr_name,
               'ubuntu:14.04', 'python3', '-c', code],
              stdout=PIPE)
    out = p.stdout.read()
    return out

def purge(ctr_name="any_name"):
#    if p.wait() == -9:  # Happens on timeout
        # We have to kill the container since it still runs
        # detached from Popen and we need to remove it after because
        # --rm is not working on killed containers
    kill_and_remove(ctr_name)

def main2():

    vals = "one two three"

    for cn in vals.split():
        print "running: ", cn
    #    execute ("print('test')", cn)
    #    assert execute("print('test1')", cn) == 'test1\n'
        assert launch("print('test1')", cn) == 'test1\n'
        print psutil.cpu_percent(interval=1, percpu=False),
        print psutil.cpu_percent(interval=1, percpu=True)
        time.sleep(1)

    #~ for cn in vals.split():
        #~ print "purging: ", cn
        #~ purge (cn)
        #~ print psutil.cpu_percent(interval=1, percpu=False),
        #~ print psutil.cpu_percent(interval=1, percpu=True)

    #assert execute("print('test1')") == 'test1\n'
    #assert execute("while True: print('test2')").startswith('test2\n' * 100)

if __name__ == '__main__':
    main2()


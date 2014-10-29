#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# mk-docktest-01.py 2014-10-30 1.1.1-2
# (C) Mikhail (myke) Kolodin, 2014
# test own tests acc to ofic docs - OK

import time
import docker
import psutil

def crecont (dc, name="noname"):
    """ create container """
    print "create container [%s], " % name,
    try:
        ctr = dc.create_container('ubuntu:14.04', name=name, )
        print "created container, "

        print "starting, ",
        dc.start(ctr)
        print "started, "

        print psutil.cpu_percent(percpu=False),
        print psutil.cpu_percent(percpu=True)

        print "virtual memory used %d%:" % psutil.virtual_memory().percent
        print "swap memory used %d%: " % psutil.swap_memory().percent

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

        names = ['ctr-'+str(n) for n in xrange(10)]

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

    return 0

if __name__ == '__main__':
    main1()

#http://serverascode.com/2014/06/05/docker-python.html

#~ making client,  client ready,
#~ version:  {u'KernelVersion': u'3.13.0-24-generic', u'Arch': u'amd64', u'ApiVersion': u'1.14', u'Version': u'1.2.0', u'GitCommit': u'fa7b24f', u'Os': u'linux', u'GoVersion': u'go1.3.1'}
#~ proc ctr [mycont-3]:
#~ create container [mycont-3],  created container,  starting,  started,  {u'HostsPath': u'/var/lib/docker/containers/27ffbc24e8533a339e048b074044bb561ee4402f5ba830c685e4855c3aa29ea1/hosts', u'Created': u'2014-10-29T15:51:13.421174218Z', u'Image': u'c4ff7513909dedf4ddf3a450aea68cd817c42e698ebccf54755973576525c416', u'Args': [], u'Driver': u'aufs', u'HostConfig': {u'CapDrop': None, u'PortBindings': None, u'NetworkMode': u'', u'Links': None, u'LxcConf': None, u'ContainerIDFile': u'', u'Devices': None, u'CapAdd': None, u'Binds': None, u'RestartPolicy': {u'MaximumRetryCount': 0, u'Name': u''}, u'PublishAllPorts': False, u'Dns': None, u'DnsSearch': None, u'Privileged': False, u'VolumesFrom': None}, u'MountLabel': u'', u'VolumesRW': {}, u'State': {u'Pid': 28093, u'Paused': False, u'Running': True, u'FinishedAt': u'0001-01-01T00:00:00Z', u'Restarting': False, u'StartedAt': u'2014-10-29T15:51:13.546260682Z', u'ExitCode': 0}, u'ExecDriver': u'native-0.2', u'ResolvConfPath': u'/var/lib/docker/containers/27ffbc24e8533a339e048b074044bb561ee4402f5ba830c685e4855c3aa29ea1/resolv.conf', u'Volumes': {}, u'Path': u'/bin/bash', u'HostnamePath': u'/var/lib/docker/containers/27ffbc24e8533a339e048b074044bb561ee4402f5ba830c685e4855c3aa29ea1/hostname', u'ProcessLabel': u'', u'Config': {u'MemorySwap': 0, u'Hostname': u'27ffbc24e853', u'Entrypoint': None, u'PortSpecs': None, u'Memory': 0, u'OnBuild': None, u'OpenStdin': False, u'Cpuset': u'', u'Env': [u'HOME=/', u'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'], u'User': u'', u'CpuShares': 0, u'AttachStdout': True, u'NetworkDisabled': False, u'WorkingDir': u'', u'Cmd': [u'/bin/bash'], u'StdinOnce': False, u'AttachStdin': False, u'Volumes': None, u'Tty': False, u'AttachStderr': True, u'Domainname': u'', u'Image': u'ubuntu:14.04', u'ExposedPorts': None}, u'Id': u'27ffbc24e8533a339e048b074044bb561ee4402f5ba830c685e4855c3aa29ea1', u'NetworkSettings': {u'Bridge': u'docker0', u'PortMapping': None, u'Gateway': u'172.17.42.1', u'IPPrefixLen': 16, u'IPAddress': u'172.17.0.87', u'Ports': {}}, u'Name': u'/mycont-3'}
#~ killing container [mycont-3],  killed,  all done


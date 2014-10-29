#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# mk-docktest-01.py 2014-10-30 1.1
# (C) Mikhail (myke) Kolodin, 2104
# test own tests acc to ofic docs - OK

import time
import docker
import psutil
from pprint import pprint as pp

def main1():
    try:
        print "making client, ",
        c = docker.Client(base_url='unix://var/run/docker.sock',
            version='1.14',
            timeout=10)
        print "client ready, "

        print "create container, ",
        ctr = c.create_container('ubuntu:14.04', name="hello-2", command='env', environment={'vasya': 'pupking'}, ports=[80, 8080])
        print "created container, ",

        print "starting, ",
        c.start(ctr, port_bindings={80:6080, 8080:6081})
        print "started, ",

        pp(c.info())
        pp(c.inspect_container(ctr))
#        print c.info()
#        print c.inspect_container(ctr)

        print "killing, ",
#        c.kill(ctr)
        c.stop(ctr)
        c.remove_container(ctr)
        print "killed, ",

        v = c.version()
        print v
    except:
        print "bad docker"

    return 0

if __name__ == '__main__':
    main1()

#http://serverascode.com/2014/06/05/docker-python.html

#~ making client,  client ready,
#~ create container,  created container,  starting,  started, {u'Containers': 1,
 #~ u'Debug': 0,
 #~ u'Driver': u'aufs',
 #~ u'DriverStatus': [[u'Root Dir', u'/var/lib/docker/aufs'], [u'Dirs', u'257']],
 #~ u'ExecutionDriver': u'native-0.2',
 #~ u'IPv4Forwarding': 1,
 #~ u'Images': 255,
 #~ u'IndexServerAddress': u'https://index.docker.io/v1/',
 #~ u'InitPath': u'/usr/bin/docker',
 #~ u'InitSha1': u'',
 #~ u'KernelVersion': u'3.13.0-24-generic',
 #~ u'MemoryLimit': 1,
 #~ u'NEventsListener': 0,
 #~ u'NFd': 15,
 #~ u'NGoroutines': 13,
 #~ u'OperatingSystem': u'Ubuntu 14.04.1 LTS',
 #~ u'SwapLimit': 0}
#~ {u'Args': [],
 #~ u'Config': {u'AttachStderr': True,
             #~ u'AttachStdin': False,
             #~ u'AttachStdout': True,
             #~ u'Cmd': [u'env'],
             #~ u'CpuShares': 0,
             #~ u'Cpuset': u'',
             #~ u'Domainname': u'',
             #~ u'Entrypoint': None,
             #~ u'Env': [u'vasya=pupking',
                      #~ u'HOME=/',
                      #~ u'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
             #~ u'ExposedPorts': {u'80/tcp': {}, u'8080/tcp': {}},
             #~ u'Hostname': u'0000582920a3',
             #~ u'Image': u'ubuntu:14.04',
             #~ u'Memory': 0,
             #~ u'MemorySwap': 0,
             #~ u'NetworkDisabled': False,
             #~ u'OnBuild': None,
             #~ u'OpenStdin': False,
             #~ u'PortSpecs': None,
             #~ u'StdinOnce': False,
             #~ u'Tty': False,
             #~ u'User': u'',
             #~ u'Volumes': None,
             #~ u'WorkingDir': u''},
 #~ u'Created': u'2014-10-29T18:08:28.152346779Z',
 #~ u'Driver': u'aufs',
 #~ u'ExecDriver': u'native-0.2',
 #~ u'HostConfig': {u'Binds': None,
                 #~ u'CapAdd': None,
                 #~ u'CapDrop': None,
                 #~ u'ContainerIDFile': u'',
                 #~ u'Devices': None,
                 #~ u'Dns': None,
                 #~ u'DnsSearch': None,
                 #~ u'Links': None,
                 #~ u'LxcConf': None,
                 #~ u'NetworkMode': u'',
                 #~ u'PortBindings': {u'80/tcp': [{u'HostIp': u'',
                                                #~ u'HostPort': u'6080'}],
                                   #~ u'8080/tcp': [{u'HostIp': u'',
                                                  #~ u'HostPort': u'6081'}]},
                 #~ u'Privileged': False,
                 #~ u'PublishAllPorts': False,
                 #~ u'RestartPolicy': {u'MaximumRetryCount': 0, u'Name': u''},
                 #~ u'VolumesFrom': None},
 #~ u'HostnamePath': u'/var/lib/docker/containers/0000582920a3e3ee9059cb9ed057e131709a4e0c2d507e68a331c80055be70ab/hostname',
 #~ u'HostsPath': u'/var/lib/docker/containers/0000582920a3e3ee9059cb9ed057e131709a4e0c2d507e68a331c80055be70ab/hosts',
 #~ u'Id': u'0000582920a3e3ee9059cb9ed057e131709a4e0c2d507e68a331c80055be70ab',
 #~ u'Image': u'c4ff7513909dedf4ddf3a450aea68cd817c42e698ebccf54755973576525c416',
 #~ u'MountLabel': u'',
 #~ u'Name': u'/hello-2',
 #~ u'NetworkSettings': {u'Bridge': u'docker0',
                      #~ u'Gateway': u'172.17.42.1',
                      #~ u'IPAddress': u'172.17.6.194',
                      #~ u'IPPrefixLen': 16,
                      #~ u'PortMapping': None,
                      #~ u'Ports': {u'80/tcp': [{u'HostIp': u'0.0.0.0',
                                              #~ u'HostPort': u'6080'}],
                                 #~ u'8080/tcp': [{u'HostIp': u'0.0.0.0',
                                                #~ u'HostPort': u'6081'}]}},
 #~ u'Path': u'env',
 #~ u'ProcessLabel': u'',
 #~ u'ResolvConfPath': u'/var/lib/docker/containers/0000582920a3e3ee9059cb9ed057e131709a4e0c2d507e68a331c80055be70ab/resolv.conf',
 #~ u'State': {u'ExitCode': 0,
            #~ u'FinishedAt': u'0001-01-01T00:00:00Z',
            #~ u'Paused': False,
            #~ u'Pid': 26476,
            #~ u'Restarting': False,
            #~ u'Running': True,
            #~ u'StartedAt': u'2014-10-29T18:08:28.302271237Z'},
 #~ u'Volumes': {},
 #~ u'VolumesRW': {}}
#~ killing,  killed,  {u'KernelVersion': u'3.13.0-24-generic', u'Arch': u'amd64', u'ApiVersion': u'1.14', u'Version': u'1.2.0', u'GitCommit': u'fa7b24f', u'Os': u'linux', u'GoVersion': u'go1.3.1'}
#~
#~
#~ ------------------
#~ (program exited with code: 0)
#~ Press return to continue

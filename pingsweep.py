#!/usr/bin/python

import os, sys, subprocess

#Syntax python pingsweep.py 192.168.0.0-10
net = sys.argv[1]
net_split = net.rsplit(".",1)
range_start = net_split[1].split("-")[0]
range_end = net_split[1].split("-")[1]

with open(os.devnull, "wb") as limbo:
        for n in xrange(int(range_start),int(range_end)):
                ip=net_split[0]+"."+format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"

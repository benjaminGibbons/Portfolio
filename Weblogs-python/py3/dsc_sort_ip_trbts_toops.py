#!/usr/bin/python

import sys
import re
toops =[]
for n in sys.stdin.readlines():
        ip = n.split(None,1)[0]
        tbytes = n.split(None,1)[1]
        toop = (ip,tbytes)
        toops.append(toop)
toops = sorted(toops, key = lambda toop: toop[1], reverse=True)
for toop in toops:
    sys.stdout.write(toop[0]+' '+toop[1])
sys.stdout.flush()
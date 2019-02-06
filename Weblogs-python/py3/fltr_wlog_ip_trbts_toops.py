#!/usr/bin/python

import sys
import re

for n in sys.stdin.readlines():
        ip = n.split(None,1)[0]
        tbytes = re.search(r'(?:\d\s{1})(\d+)',n)
        if tbytes != None:
            toop = (ip,tbytes.group(1))
        else:
            toop = (ip, '0')
        sys.stdout.write(toop[0]+' '+toop[1]+' \n')
sys.stdout.flush()

#!/usr/bin/python3
import sys
import re

for n in sys.stdin.readlines():
        tbytes = re.search(r'(?:\d\s{1})(\d+)',n)
        if tbytes !=None:
            sys.stdout.write(tbytes.group(1)+' \n')
        else:
            sys.stdout.write('0 \n')
sys.stdout.flush()
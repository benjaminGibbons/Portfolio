#!/usr/bin/python

import sys
import re


code = sys.argv[1]
pattern = re.compile(r'(?:\s)(\d{3})(?:\s)')
for n in sys.stdin.readlines():
     fcode=re.search(pattern,n)
     if code == fcode.group(1):
        sys.stdout.write(n)

sys.stdout.flush()
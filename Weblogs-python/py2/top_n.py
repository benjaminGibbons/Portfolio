#!/usr/bin/python

import sys

i = int(sys.argv[1])
for x in range(0,i):
    n = sys.stdin.readline()
    sys.stdout.write(n)
sys.stdout.flush()
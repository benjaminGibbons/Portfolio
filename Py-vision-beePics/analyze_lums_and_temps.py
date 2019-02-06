##Yes, luminosity and temp are positively correlated r = .905. This makes sense since bright days tend to be warmer.  
import argparse
import cv2
import sys
import os
import fnmatch
import re

ap = argparse.ArgumentParser()
ap.add_argument('-lf', '--lum_file', required = True, help = 'Path to lum file')
ap.add_argument('-tf', '--temp_file', required = True, help = 'Path to temp file')
args = vars(ap.parse_args())

## define regexes
lum_entry_pat  = r'(?:.*_)(\d\d)(?:-\d\d-\d\d\.\w+\s*)(\d+\..*)'
temp_entry_pat = r'(?:.*_)(\d\d)(?:-\d\d-\d\d\s)(\d+\..*)'

## define two dictionaries
lum_tbl = {}
tmp_tbl = {}

with open(args['lum_file']) as infile:
    for line in infile:
        m = re.match(lum_entry_pat, line)
        if m != None:
            hr = m.group(1)
            lum = m.group(2)
            if hr in lum_tbl:
                lum_tbl[hr].append(float(lum))
            else:
                lum_tbl[hr]=[float(lum)]
with open(args['temp_file']) as infile:
    for line in infile:
        m = re.match(temp_entry_pat, line)
        if m != None:
            hr = m.group(1)
            tmp = m.group(2)
            if hr in tmp_tbl:
                tmp_tbl[hr].append(float(tmp))
            else:
                tmp_tbl[hr]=[float(tmp)]

## print tables and averages
print('Luminosity Table')
for h, lums in lum_tbl.items():
    print h, '-->', str(lums)
print

print('Temperature Table')
for h, temps in tmp_tbl.items():
    print h, '-->', str(temps)
print

print('Luminosity Averages')
for h, lums in lum_tbl.items():
    print h, '-->', sum(lums)/len(lums)
print

print('Temperature Averages')
for h, temps in tmp_tbl.items():
    print h, '-->', sum(temps)/len(temps)
print



       


    


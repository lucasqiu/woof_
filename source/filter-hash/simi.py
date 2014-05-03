#!/usr/bin/python

import os
import sys
import subprocess
import re

f = open('similarities.csv', 'r')
r = open('simi.txt', 'w')
arr = []
for line in f:
    #print line
    a = re.findall(r"[\w'\.]+", line)
    if (len(a)>4 and float(a[3])>0.1):
        f1 = a[0]
        f2= a[1]
        r.write(f1+' '+f2+'\n')

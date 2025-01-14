# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys
print (sys.argv )

from dredlock import Dredlock

try:
    key = sys.argv[1]
except IndexError:
    key = "jobs"
  
try:
    val = sys.argv[2]
except IndexError:
    val = "test"  
    
    
hhh = Dredlock()

print ('pushing {} to {}'.format(val, key))

hhh.r.rpush(key, val)

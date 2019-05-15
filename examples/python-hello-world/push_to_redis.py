# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys
print sys.argv 

from hungry_hungry_hippos import HungryHungryHippos

try:
    key = sys.argv[1]
except IndexError:
    key = "jobs"
  
try:
    val = sys.argv[2]
except IndexError:
    val = "test"  
    
    
hhh = HungryHungryHippos()

print 'pushing {} to {}'.format(val, key)

hhh.r.rpush(key, val)

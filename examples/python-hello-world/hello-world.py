# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys

print sys.argv 

from lib.hungry_hungry_hippos import HungryHungryHippos

keys = ("jobs")
hhh = HungryHungryHippos()

print 'connecting to redis'

while True:
    print 'while true'
    (k,v) = hhh.blpop(keys)
    print "got a {} {}".format(k,v)
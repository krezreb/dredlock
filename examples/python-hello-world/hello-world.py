#!/usr/bin/python3

# -*- coding: utf-8 -*-

import os, sys

print (sys.argv )

from dredlock import Dredlock

keys = ("jobs")
hhh = Dredlock()

print('Entering while true loop, awaiting messages')
while True:
    (k,v) = hhh.blpop(keys)
    print("Received value {} in list {}".format(v,k))
    
    # Here is where you can put your application code that does the actual work
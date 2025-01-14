# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys

from hungry_hungry_hippos import HungryHungryHipposCatchSignals

keys = ("jobs")
hhh = HungryHungryHipposCatchSignals()

print ('connecting to redis')

import signal
import time

def exit_gracefully(signum, frame):
    print('Caught a signal {}, exiting'.format(signum))
    exit()

signal.signal(signal.SIGTERM, exit_gracefully)

print ('Entering while true loop')

while True:
    print ('blpop...')
    (k,v) = hhh.blpop(keys)
    print ("got a {} {}".format(k,v))
    time.sleep(1)

  
  

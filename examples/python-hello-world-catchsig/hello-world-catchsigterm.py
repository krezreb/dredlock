# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys

print sys.argv 

from hungry_hungry_hippos import HungryHungryHipposCatchSignals

keys = ("jobs")
hhh = HungryHungryHipposCatchSignals()

print 'connecting to redis'

import signal
import time

class GracefulKiller(object):
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        print 'got a sig {}'.format(signum)
        self.kill_now = True
    

killer = GracefulKiller()

while True:
    print 'while true'
    (k,v) = hhh.blpop(keys)
    print "got a {} {}".format(k,v)
    time.sleep(1)
    if killer.kill_now:
        print "just got told to quit. Exiting"
        break
  
  

# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys

print sys.argv 

from lib.hungry_hungry_hippos import HungryHungryHippos

keys = ("jobs")
hhh = HungryHungryHippos()

print 'connecting to redis'

import signal
import time

class GracefulKiller:
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
        print "Whoa I just got told to quit.  Sir yes sir!"
        break
  
  

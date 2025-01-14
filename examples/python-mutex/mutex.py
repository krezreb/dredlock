# -*- coding: utf-8 -*-

import os, sys

import time
import random 
from dredlock import Dredlock

key="locks"
val="foo"

lock_lists = (key)
hhh = Dredlock()

# here we make the lock
hhh.r.rpush(key, val)

print("Random sleep so that an arbitrary instance will get the lock")
time.sleep(random.uniform(0.5, 1.9))

# here we try and acquire the lock
(gotlock, k, v) = hhh.blpop_lock(lock_lists)
if gotlock:
    try:
        print(u"GOT LOCK {} with value {}".format(k,v))
        
        # your application code that does the work goes here
        time.sleep(1)
        print(u"During this time only this instance will operate on this given lock/value pair")

        time.sleep(1)
        
        
        countdown = list(reversed(range(1, 6)))
        for c in countdown:
            print(u"Releasing lock in {}...".format(c))

            time.sleep(1)
                   
        
    except Exception as e:
        # if something goes wrong we should release the lock and/or do something else
        hhh.release_lock(v)
    
    print(u"Releasing lock")
    hhh.release_lock(v)
else:
    print(u"Some other process already has a lock on list {} with value {}".format(k, v))

    # presumably here you do nothing
    print(u'Waiting for lock to be released')
    hhh.wait_for_lock(v, 30)
    print(u'Lock {} has been released'.format(v))
    
    
    
print(u'Quitting')
exit(0)
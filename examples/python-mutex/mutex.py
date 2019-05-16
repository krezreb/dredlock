# -*- coding: utf-8 -*-

import os, sys
print sys.argv 
import time

from hungry_hungry_hippos import HungryHungryHippos

key="locks"
val="foo"

lock_lists = (key)
hhh = HungryHungryHippos()

# here we make the lock
hhh.r.rpush(key, val)

# here we try and acquire the lock
(gotlock, k, v) = hhh.blpop_lock(lock_lists)
if gotlock:
    try:
        print(u"Successfully locked list {} with value {}".format(k,v))
        
        # your application code that does the work goes here
        time.sleep(1)
        print(u"During this time only this instance will operate on this given lock/value pair")

        time.sleep(1)
        
        print(u"Releasing lock in")
        
        countdown = range(1,6)
        countdown.reverse()
        for c in countdown:
            print(c)
            time.sleep(1)
                   
        
    except Exception as e:
        # if something goes wrong we should release the lock and/or do something else
        hhh.release_lock(v)
    
    print(u"Done, releasing lock")
    hhh.release_lock(v)
else:
    print(u"Some other process already has a lock on list {} with value {}".format(k, v))

    # presumably here you do nothing
    print(u'Waiting for lock to be released')
    hhh.wait_for_lock(v)
    print(u'Lock {} has been released'.format(v))
    
    
    
print(u'Quitting')
exit(0)
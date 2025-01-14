# -*- coding: utf-8 -*-

import os, sys
print sys.argv 
import time


REDIS_NAMESPACE=os.getenv('REDIS_NAMESPACE', 'default')
REDIS_HOST=os.getenv('REDIS_HOST', '127.0.0.1')

REDIS_HOST_0=os.getenv('REDIS_HOST_0', '127.0.0.1')
REDIS_HOST_1=os.getenv('REDIS_HOST_1', '127.0.0.1')


REDIS_PORT=os.getenv('REDIS_PORT', 6379)

from dredlock import Dredlock

key="locks hey there: 1 bro -f"
val=1

from rediscluster import RedisCluster


print REDIS_HOST

startup_nodes = [{"host": REDIS_HOST_0, "port": REDIS_PORT},{"host": REDIS_HOST_1, "port": REDIS_PORT}]


rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)

hhh = Dredlock(redis_client=rc, namespace=REDIS_NAMESPACE)
    
lock_lists = (key)

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
        
        countdown = range(1,2)
        countdown.reverse()
        for c in countdown:
            print(c)
            time.sleep(1)
                   
        
    except Exception as e:
        # if something goes wrong we should release the lock and/or do something else
        print e
        hhh.release_lock(v)
    
    #print(u"Done, releasing lock")
    #hhh.release_lock(v)
else:
    print(u"Some other process already has a lock on list {} with value {}".format(k, v))

    # presumably here you do nothing
    print(u'Waiting for lock to be released')
    hhh.wait_for_lock(v)
    print(u'Lock {} has been released'.format(v))
    
    
hhh.cleanup()
print(u'Quitting')

# -*- coding: utf-8 -*-
#!/usr/bin/python

import redis
import time
import threading

class HungryHungryHippos(object):
    
    def __init__(self, host='redis', port=6379, db=0):
        self.r = redis.StrictRedis(host=host, port=port, db=db)
    
    def _getkeys(self, k):
        lock_key = u'{}:{}'.format(k,'lock')
        keepalive_key = u'{}:{}'.format(k,'keepalive')
        
        return (lock_key, keepalive_key)

    def release_lock(self, v):
        #print u'Releasing lock {}'.format(v)
        (lock_key, keepalive_key) = self._getkeys(v)

        pipe = self.r.pipeline()
        pipe.expire(lock_key, '0')
        pipe.expire(keepalive_key, '0')
        pipe.execute()
        
    def lock_keepalive(self, v, lock_uuid, sleep=10):
        print u'Starting lock renewal thread for {} with uuid={}'.format(v, lock_uuid)
        (lock_key, keepalive_key) = self._getkeys(v)
        
        pipe = self.r.pipeline()
        pipe.llen(lock_key) # len of lock
        pipe.lrem(keepalive_key, 0, lock_uuid) # remove my unique key from lock to get the len
        pipe.rpush(keepalive_key, lock_uuid)   # put it back
        result = pipe.execute()
        
        #print result
        
        while True:
            if result[0] == 0:
                # lock no longer exists
                print u'lock {} disappeared'.format(lock_key)
                return
            
            if result[1] == 0:
                # my keepalive_key no longer exists
                print u'keepalive_key {} disappeared'.format(keepalive_key)
                return
            
            #print u'renewing lock {} to expire in {} seconds'.format(keepalive_key, sleep*2)
            # set it to expire further in the future
            self.r.expire(keepalive_key, sleep*2)   
            time.sleep(sleep)

    def _get_lock_uuid(self):
        return "{}".format(float(time.time()))
        
    @property
    def thread(self):
        return self.t
    
    
    def blpop_lock(self, keys=[]):
        (k,v) = self.r.blpop(keys, 0)

        (lock_key, keepalive_key) = self._getkeys(v)
        
        #print (u"got a {}".format(v))
        
        lock_uuid = self._get_lock_uuid()
        
        #print "v={} lock_uuid={}".format(v, lock_uuid)
        
        pipe = self.r.pipeline()
        pipe.rpush(lock_key, lock_uuid)
        pipe.rpush(keepalive_key, lock_uuid)
        pipe.expire(keepalive_key, 3) # queue for long expiry right away
        result = pipe.execute()
        
        #print result
        
        if result[0] == 1:
            # lock queue only has one item in it (mine!)
            # I have the lock
            print ("Got lock {}".format(lock_key))
            self.t = threading.Thread(target=self.lock_keepalive, args=(v,lock_uuid,))
            self.t.start()
    
            lock_success = True
        else :
            lock_success = False

            if result[1] == 1:
                # no previous keepalive lock, looks like I got a stale lock
                self.release_lock(v)
                
                # put it back on the shelf for the next person
                self.r.lpush(k,v)
                # I don't have the lock
                print ("Found a stale lock {} putting it back in the front of the line".format(v))
                
            else:
                # I don't have the lock
                print ("{} already locked".format(lock_key))
                
            
        return (lock_success, k, v)


# -*- coding: utf-8 -*-

"""
app supervisor - heartbeat checker
"""

import time
import random

#fix
#import dateutil
import arrow
import redis

#fix
import greenlet

import gevent
from gevent import Timeout
from gevent.pool import Pool

from logbook import Logger
log = Logger('heartbeat')

log.info('start')


#redis pool
REDIS_MAX_CONNECTIONS = 100

rpool = redis.ConnectionPool(host='localhost', port=6379, db=1, \
            max_connections=REDIS_MAX_CONNECTIONS)

rclient = redis.Redis(connection_pool=rpool) 


class TimeoutException(Exception):
    """ timeout exception for gevent Timeout"""
    pass

class Point(object):
    """ Data Point"""
    def __init__(self):
        pass
    
def start(name):
    """start time"""
    timestamp =  time.time()
    rclient.set("%s.start" % (name), timestamp)    

def heartbeat(name):
    """heartbeat to redis"""
    timestamp =  time.time()
    rclient.set(name, timestamp) 
    print ( "%s:%s" % (name, timestamp) )
    
def sendmail(msg):    
    """send mail"""
    print(msg)    
    
def restart(name):
    """restart process / service"""
    msg = "restart [%s]" % (name)
    alert(msg)
    print(msg)
    
def alert(msg):
    """
    put info to redis here
    """
    sendmail(msg)



def func1():
    
        
    utc = arrow.utcnow()
    local = utc.to('Asia/Shanghai')
    ts = local.timestamp
    print arrow.get(ts)
    #print local.format('YYYY-MM-DD HH:mm:ss ZZ')
    
    """function and heartbeat"""
    
    ex = TimeoutException("timeout ex")
    
    #gevent timeout
    timeout = Timeout(6, ex)
    #start
    timeout.start()
    try:
        
        # exception will be raised here, after *seconds* 
        # passed since start() call
        
        gevent.sleep(3 * random.randint(1,4))
        #print "f1 heart beat"
        heartbeat("f1")

    except TimeoutException as ex:
        print ex
    finally:
        #cancel timeout
        timeout.cancel()

def main():

    """spawn"""    
     
    val = rclient.get('f1')   

    print(val)
    
    pool = Pool(20)
    
    start('f1')
    

    
    
    #loop forever
    while True:
        
        #print( time.time() )        
        pool.spawn(func1)
        #print pool.wait_available()
        print ( pool.free_count() )
        
        #sleep
        gevent.sleep(2)        
        

if __name__ == "__main__":
    
    main()
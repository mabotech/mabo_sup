
"""supersior, check if heartbeat of app stoped"""

import time
import gevent


import redis

#app_server

#restart_strategy

#register

SLEEP_SECONDS = 5

HEARTBEAT_INTERVAL = 1

THRESHHOLD = 10

LAST_ALERT = ""

TOTAL_ALERT_TH = 3

# send email 
# stop alert if total alert > threadhold

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0


class Supervisor(object):
    """class"""
    
    def __init__(self):
        
        self.app_list = ["app1", "app2", "app3"]
                
        self.rclient = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, \
                                        db=REDIS_DB)
    
    def add_app(self):
        """add app while running
        impl: check etcd and get app list every minute?
        
        """
        
        pass
        
    def remove_app(self):
        """remove app whild running"""
        
        pass
    
    @classmethod      
    def notify(cls, app, msg):
        
        """
        send restart msg
        """
        
        #self.rclient.lpush()
        
        print("[%s,%s]send alert to job queue" % (app, msg))
    
    @classmethod
    def has_issue(cls, now, last_heartbeat):
        
        """check if heartbeat stoped"""
        
        delta = now - last_heartbeat
        
        if delta > THRESHHOLD:
            return True
        else:
            return False    


    def check(self, app):
        
        """check app heartbeat"""
        
        val = self.rclient.get("aac")
        
        now = time.time()
        
        self.rclient.set("check_hb", now)
        
        print (val)
        
        if self.has_issue(now, 0):
            msg = ""
            self.notify(app, msg)
        
    
    def run(self):        
        """supervisor, check heartbeart & restart """        
        #

        
        # forever loop
        while True:            
            
            for app in self.app_list:
                self.check(app)               
            #print("check")
            
            gevent.sleep(SLEEP_SECONDS)
        
    
    
def main():
    """main"""
    supervisor = Supervisor()
    supervisor.run()
    
    
if __name__ == "__main__":
    main()
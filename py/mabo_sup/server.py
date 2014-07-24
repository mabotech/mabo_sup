
import time

from flask import Flask

import redis

REDIS_MAX_CONNECTIONS = 100

rpool = redis.ConnectionPool(host='localhost', port=6379, db=1, \
            max_connections=REDIS_MAX_CONNECTIONS)

rclient = redis.Redis(connection_pool=rpool) 

app = Flask(__name__)

@app.route("/")
def hello():
    t = rclient.get("f1")
    d = time.time() - float(t)
    #msg = "heartbeat:" + t + "/" + d
    return "%s" % (d)

if __name__ == "__main__":
    app.run(port=8026)
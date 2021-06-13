from flask import Flask, make_response
from Queue import Queue
import time
import functools
import os

app = Flask(__name__)
queueing = Queue(maxsize=os.getenv("QUEUE_SIZE"))

def multiple_control(q):
    def _multiple_control(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            q.put(time.time())
            result = func(*args,**kwargs)
            q.get()
            q.task_done()
            return result

        return wrapper
    return _multiple_control

@app.route('/', methods=['GET'])
@multiple_control(queueing)
def root():
    print("[GET] root")
    return(make_response('end root'))

@app.route('/slow', methods=['GET'])
@multiple_control(queueing)
def slow():
    print('[GET] slow')
    time.sleep(10)
    return(make_response('end slow'))

if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        threaded=True
    )
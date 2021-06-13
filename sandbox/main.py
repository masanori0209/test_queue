from flask import Flask, make_response
from Queue import Queue
import time
import functools

app = Flask(__name__, static_folder=None)
queueing = Queue(maxsize=os.envget("QUEUE_SIZE"))

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
@multiple_control(singleQueue)
def root():
    print("[GET] root")
    return(make_response('end root'))

@app.route('/slow', methods=['GET'])
@multiple_control(singleQueue)
def slow():
    print('[GET] slow')
    time.sleep(10)
    return(make_response('end slow'))

if __name__ == "__main__":
    app.run(
        host='localhost',
        port=3000,
        threaded=True
    )
from flask import Flask
import time
import sys
import threading
import os 
import signal

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


def stop_flask(pid):
    time.sleep(10)
    os.kill(pid, signal.SIGINT)

#TODO: PASS DEBUG FLAG AS ARGUMENT
if __name__ == '__main__':
    debug = False
    if sys.argv[1]:
        print("starting, killing ")
        t = threading.Thread(target=stop_flask, args=(os.getpid(),))
        t.start()
        debug = True
    app.run(port=3000, debug=debug)

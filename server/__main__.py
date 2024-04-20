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


def stop_flask():
    time.sleep(10)
    print("timesup")
    os.kill(os.getpid(), signal.SIGINT)

#TODO: PASS DEBUG FLAG AS ARGUMENT
if __name__ == '__main__':
    debug = False
    if sys.argv[1]:
        print("starting, killing ")
        t = threading.Thread(target=stop_flask)
        t.start()
        debug = True
    app.run(port=3000, debug=debug)

    print("starting, killing ")
    time.sleep(10)
    print("timesup")
    os.kill(os.getpid(), signal.SIGINT)

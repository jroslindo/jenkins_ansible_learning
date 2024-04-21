from flask import Flask
import time
import sys
import threading
import os 
import signal

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><h1>Final test working!!!!!!!!!!!!!!!!!</h1>'


def stop_flask(pid):
    print("starting, killing!!!")
    # time.sleep(10)
    print("pid", pid)
    os.kill(pid, signal.SIGINT)

#TODO: PASS DEBUG FLAG AS ARGUMENT
if __name__ == '__main__':
    # debug = False
    # if sys.argv[1]:
        
    #     t = threading.Thread(target=stop_flask, args=(os.getpid(),))
    #     t.start()
    #     debug = True
    app.run(host='0.0.0.0', port=3000, debug=True)

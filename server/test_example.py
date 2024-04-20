import unittest
import threading
import time
import subprocess
import sys
import requests
import signal

def get_request(url):
    response = requests.get(url)
    return response.status_code

class TestGetRequest(unittest.TestCase):
    def test_get_request_working(self):
        url = 'http://localhost:3000'
        status_code = get_request(url)
        self.assertEqual(status_code, 200)

    # def test_get_request_not_working(self):
    #     url = 'http://localhost:3000/test'
    #     status_code = get_request(url)
    #     self.assertEqual(status_code, 200)


def threadingApplication():
    process = subprocess.run("$HOME/.local/bin/poetry run python3 __main__.py true", shell=True)
    # time.sleep(10)
    print("Asking to kill")
    process.send_signal(signal.SIGINT)
    print("finished!!!")


if __name__ == '__main__':
    # thread = threading.Thread(target=threadingApplication)
    # thread.start()
    # time.sleep(5)
    unittest.main()

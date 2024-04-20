import requests
import unittest
import threading
import time
import subprocess
import sys

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
    subprocess.run("python server\__main__.py", shell=True)
    print("process finished")


if __name__ == '__main__':
    thread = threading.Thread(target=threadingApplication)
    thread.start()
    time.sleep(5)
    unittest.main()
    print("closing")
    sys.exit()
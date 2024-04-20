import requests
import unittest

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

if __name__ == '__main__':
    unittest.main()

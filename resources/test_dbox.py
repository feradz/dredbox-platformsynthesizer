import unittest
import requests


class TestDboxApi(unittest.TestCase):

    def testDboxInfo(self):
        url = "http://localhost:5003/api/dbox/info"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1]',  response.json())

    def testDboxTemperature(self):
        url = "http://localhost:5003/api/dbox/temperature"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1]',  response.json())

    def testDboxPower(self):
        url = "http://localhost:5003/api/dbox/power"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1]',  response.json())

    def testDboxFanSpeed(self):
        url = "http://localhost:5003/api/dbox/fanspeed"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1]',  response.json())

    def testDboxFanPing(self):
        url = "http://localhost:5003/api/dbox/ping"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1]',  response.json())


if __name__ == '__main__':
    unittest.main()

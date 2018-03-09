import unittest
import requests


class TestDboxApi(unittest.TestCase):

    def testDboxInfo(self):
        url = "http://localhost:5003/api/dbox/info"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1]')

    def testDboxTemperature(self):
        url = "http://localhost:5003/api/dbox/temperature"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1]')

    def testDboxPower(self):
        url = "http://localhost:5003/api/dbox/power"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1]')

    def testDboxFanSpeed(self):
        url = "http://localhost:5003/api/dbox/fanspeed"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1]')

    def testDboxFanPing(self):
        url = "http://localhost:5003/api/dbox/ping"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1]')


if __name__ == '__main__':
    unittest.main()

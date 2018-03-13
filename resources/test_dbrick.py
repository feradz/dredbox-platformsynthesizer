import unittest
import requests


class TestDbrickApi(unittest.TestCase):

    def testDbrickSwitchOn(self):
        url = "http://localhost:5003/api/dbrick/switchon"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickSwitchOff(self):
        url = "http://localhost:5003/api/dbrick/switchoff"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickIsOn(self):
        url = "http://localhost:5003/api/dbrick/ison"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickInfo(self):
        url = "http://localhost:5003/api/dbrick/info"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickPower(self):
        url = "http://localhost:5003/api/dbrick/power"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickGetBootSource(self):
        url = "http://localhost:5003/api/dbrick/getbootsource"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickSetBootSource(self):
        url = "http://localhost:5003/api/dbrick/setbootsource"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11", "path":"/dev/sda","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertNotIn('Error', response.json())

    def testDbrickLink(self):
        url = "http://localhost:5003/api/dbrick/links"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())

    def testDbrickPing(self):
        url = "http://localhost:5003/api/dbrick/ping"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertIn('[0, 1, 11]', response.json())


if __name__ == '__main__':
    unittest.main()

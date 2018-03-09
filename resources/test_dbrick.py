import unittest
import requests


class TestDbrickApi(unittest.TestCase):

    def testDbrickSwitchOn(self):
        url = "http://localhost:5003/api/dbrick/switchon"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickSwitchOff(self):
        url = "http://localhost:5003/api/dbrick/switchoff"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickIsOn(self):
        url = "http://localhost:5003/api/dbrick/ison"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickInfo(self):
        url = "http://localhost:5003/api/dbrick/info"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickPower(self):
        url = "http://localhost:5003/api/dbrick/power"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickGetBootSource(self):
        url = "http://localhost:5003/api/dbrick/getbootsource"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickSetBootSource(self):
        url = "http://localhost:5003/api/dbrick/setbootsource"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11", "path":"/dev/sda"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11, "/dev/sda"]')

    def testDbrickLink(self):
        url = "http://localhost:5003/api/dbrick/links"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testDbrickPing(self):
        url = "http://localhost:5003/api/dbrick/ping"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')


if __name__ == '__main__':
    unittest.main()

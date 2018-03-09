import unittest
import requests


class TestSwitchApi(unittest.TestCase):

    def testSwitchInfo(self):
        url = "http://localhost:5003/api/switch/info"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertEqual(response.json(), '[0, 1, 11]')

    def testSwitchConnectPorts(self):
        url = "http://localhost:5003/api/switch/connectports"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11", "ports": "[[11,22],[12,25]]"}'
        response = requests.post(url, data=payload, headers=headers)
        with self.subTest():
            self.assertIn(response.json(), '11')
        with self.subTest():
            self.assertIn(response.json(), '22')
        with self.subTest():
            self.assertIn(response.json(), '12')
        with self.subTest():
            self.assertIn(response.json(), '25')

    def testSwitchDisconnectPorts(self):
        url = "http://localhost:5003/api/switch/disconnectports"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11", "ports": "[[11,22],[12,25]]"}'
        response = requests.post(url, data=payload, headers=headers)
        with self.subTest():
            self.assertNotIn(response.json(), '11')
        with self.subTest():
            self.assertNotIn(response.json(), '22')
        with self.subTest():
            self.assertNotIn(response.json(), '12')
        with self.subTest():
            self.assertNotIn(response.json(), '25')

    def testSwitchEndPoint(self):
        url = "http://localhost:5003/api/switch/portendpoint"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11", "portId": "11"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertEqual(1, 1)

    def testSwitchPortsInfo(self):
        url = "http://localhost:5003/api/switch/portsinfo"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertIn(response.json(), "@")


if __name__ == '__main__':
    unittest.main()

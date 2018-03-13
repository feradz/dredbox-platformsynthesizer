import unittest
import requests


class TestSwitchApi(unittest.TestCase):

    def testSwitchInfo(self):
        url = "http://localhost:5003/api/switch/info"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.get(url, data=payload, headers=headers)
        self.assertNotIn("Error", response.json())

    def testSwitchConnectPorts(self):
        url = "http://localhost:5003/api/switch/connectports"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11", "ports": "[[11,22],[12,25]]","ipAddress":"10.128.0.1","a":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertNotIn("Error", response.json())

    def testSwitchDisconnectPorts(self):
        url = "http://localhost:5003/api/switch/disconnectports"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11", "ports": "[[11,22],[12,25]]","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertNotIn("Error", response.json())

    def testSwitchEndPoint(self):
        url = "http://localhost:5003/api/switch/portendpoint"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11", "portId": "11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertNotIn("Error", response.json())

    def testSwitchPortsInfo(self):
        url = "http://localhost:5003/api/switch/portsinfo"
        headers = {'Content-Type': 'application/json'}
        payload = '{"dRackId":"0","dBoxId":"1","switchId":"11","ipAddress":"10.128.0.1","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertNotIn("Error", response.json())


if __name__ == '__main__':
    unittest.main()

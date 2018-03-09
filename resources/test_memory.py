import unittest
import requests


class TestMemoryApi(unittest.TestCase):

    def testAddRemoteMemory(self):
        url = "http://localhost:5003/api/memory/addremotememory"
        headers = {'Content-Type': 'application/json'}
        payload = '{"ComputeBrickIP":"http://localhost:5001", "memoryAddress":[{"startA":"0x41000000","endA":"0x430000000","port":21,"offset":45,"action":"Add"},{"startA":"0x45000000","endA":"0x470000000","port":21,"offset":45,"action":"Add"},{"startA":"0x48000000","endA":"0x530000000","port":21,"offset":45,"action":"Add"}],"ipAddress":"0.0.0.0","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertIn(response.json(), "echo online")

    def testRemoveRemoteMemory(self):
        url = "http://localhost:5003/api/memory/removeremotememory"
        headers = {'Content-Type': 'application/json'}
        payload = '{"ComputeBrickIP":"http://localhost:5001", "memoryAddress":[{"startA":"0x41000000","endA":"0x430000000","port":21,"offset":45,"action":"Add"},{"startA":"0x45000000","endA":"0x470000000","port":21,"offset":45,"action":"Add"},{"startA":"0x48000000","endA":"0x530000000","port":21,"offset":45,"action":"Remove"}],"ipAddress":"0.0.0.0","port":"5001"}'
        response = requests.post(url, data=payload, headers=headers)
        self.assertIn(response.json(), "echo offline")


if __name__ == '__main__':
    unittest.main()

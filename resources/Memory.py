from flask_restful import fields, marshal_with, reqparse, Resource, request
import json
import requests
import urllib2
post_parser = reqparse.RequestParser()


class MemoryTest(Resource):
    def post(self):
        memoryAddress = []
        memoryAddress2 = []
        result = []
        jsonData = request.get_json(force=True)
        url = jsonData["ComputeBrickIP"]
        url += '/RemoteMemory'
        for memAddr in jsonData["memoryAddress"]:
            action = memAddr["action"]
            startA = memAddr["startA"]
            endA = memAddr["endA"]
            port = memAddr["port"]
            offset = memAddr["offset"]
            payload = {
                "segments": [{
                    "startA": startA,
                    "endA": endA,
                    "port": port,
                    "offset": offset
                }],
                "action":
                action
            }
            if (action == "Add"):
                memoryAddress.append(memAddr)
                r = requests.post(url, data=json.dumps(payload))
                resp = r.json()
                # print(r.text)

                result.append(json.loads(resp))
            elif (action == "Remove"):
                memoryAddress2.append(memAddr)
                r = requests.post(url, data=json.dumps(payload))
                resp = r.json()
                # print(r.text)

                result.append(json.loads(resp))
            else:
                pass
        return result


class AddRemoteMemory(Resource):
    def post(self):
        jsonData = request.get_json(force=True)
        ipAddress = jsonData['ipAddress']
        port = jsonData['port']
        del jsonData['port']
        del jsonData['ipAddress']
        print(jsonData)
        url = "http://"+ipAddress+":"+port+"/api/memory/addremotememory"
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        r = urllib2.urlopen(req, json.dumps(jsonData))
        return r.read()


class RemoveRemoteMemory(Resource):
    def post(self):
        jsonData = request.get_json(force=True)
        ipAddress = jsonData['ipAddress']
        port = jsonData['port']
        del jsonData['port']
        del jsonData['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/memory/removeremotememory"
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        r = urllib2.urlopen(req, json.dumps(jsonData))
        return r.read()

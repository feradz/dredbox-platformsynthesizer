from flask_restful import fields, marshal_with, reqparse, Resource, request
import json
import requests
post_parser = reqparse.RequestParser()
post_parser2 = reqparse.RequestParser()

post_parser2.add_argument(
    'memoryAddress',
    required=True,
    help='memoryAddress', )
post_parser.add_argument(
    'startA',
    required=True,
    help='Start Address', )
post_parser.add_argument(
    'endA',
    required=True,
    help='End Address', )
post_parser.add_argument(
    'port',
    required=True,
    help='Port', )
post_parser.add_argument(
    'offset',
    required=True,
    help='Memory Offset', )
post_parser.add_argument(
    'action',
    required=True,
    help='Action', )
post_parser.add_argument(
    'ComputeBrickIP', required=True, help='Compute Brick IP')
post_parser.add_argument(
    'port',
    required=True, )
post_parser.add_argument(
    'ipAddress',
    required=True, )


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
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/memory/addremotememory"
        r = requests.post(url, data=args)
        return r.text


class RemoveRemoteMemory(Resource):
    def post(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/memory/removeremotememory"
        r = requests.post(url, data=args)
        return r.text

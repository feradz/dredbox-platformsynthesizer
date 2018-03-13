from flask_restful import fields, marshal_with, reqparse, Resource, request
import json
import requests

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'dRackId',
    type=int,
    required=True,
    help='Rack Id', )

post_parser.add_argument(
    'dBoxId',
    type=int,
    required=True,
    help='Box id', )

post_parser.add_argument(
    'switchId',
    type=int,
    required=True,
    help='Switch Id', )

post_parser.add_argument(
    'port',
    required=True, )

post_parser.add_argument(
    'ipAddress',
    required=True, )


class Switch(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/switch/info"
        r = requests.get(url, data=args)
        return r.text


class SwitchConnectPorts(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('ports', location='json')

    def post(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/switch/connectports"
        r = requests.post(url, data=args)
        return r.text


class SwitchDisconnectPort(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('ports', location='json')

    def post(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/switch/disconnectports"
        r = requests.post(url, data=args)
        return r.text


class SwitchPortEndPoint(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('ports', location='json')

    def post(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/switch/portendpoint"
        r = requests.post(url, data=args)
        return r.text


class SwitchPortsInfo(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/switch/portsinfo"
        r = requests.get(url, data=args)
        return r.text


class SwitchPowerUtilization(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/switch/powerutilization"
        r = requests.get(url, data=args)
        return r.text

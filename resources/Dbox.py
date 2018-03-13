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
    'port',
    required=True, )

post_parser.add_argument(
    'ipAddress',
    required=True, )


class Dbox(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbox/info"
        r = requests.get(url, data=args)
        return r.text


class DboxTemperature(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbox/temperature"
        r = requests.get(url, data=args)
        return r.text


class DboxPower(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbox/power"
        r = requests.get(url, data=args)
        return r.text


class DboxFanSpeed(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbox/fanspeed"
        r = requests.get(url, data=args)
        return r.text


class DboxPing(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbox/ping"
        r = requests.get(url, data=args)
        return r.text

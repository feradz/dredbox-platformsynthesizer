from flask_restful import fields, marshal_with, reqparse, Resource, request
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
    'dBrickId',
    type=int,
    required=True,
    help='Brick id', )

post_parser.add_argument(
    'port',
    required=True, )

post_parser.add_argument(
    'ipAddress',
    required=True, )


class Dbrick(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/info"
        r = requests.get(url, data=args)
        return r.text


class DbrickSwitchOn(Resource):
    def post(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/switchon"
        r = requests.post(url, data=args)
        return r.text


class DbrickSwitchOff(Resource):
    def post(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/switchoff"
        r = requests.post(url, data=args)
        return r.text


class DbrickIsOn(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/ison"
        r = requests.get(url, data=args)
        return r.text


class DbrickPower(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/power"
        r = requests.get(url, data=args)
        return r.text


class DbrickLinks(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/links"
        r = requests.get(url, data=args)
        return r.text


class DbrickPing(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/ping"
        r = requests.get(url, data=args)
        return r.text


class DbrickSetBootSource(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument(
        'path',
        type=str,
        required=True,
        help='Boot Source', )

    def post(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/setbootsource"
        r = requests.post(url, data=args)
        return r.text


class DbrickGetBootSource(Resource):
    def get(self):
        args = post_parser.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/dbrick/getbootsource"
        r = requests.get(url, data=args)
        return r.text

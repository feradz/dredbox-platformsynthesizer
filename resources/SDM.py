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


def getIPAddressFromDbrickId(dRackId, dBoxId, dBrickId):
    #TODO implement proper function to get dbrick ip address
    return "http://10.128.0.16:5001"


class InitShmem(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('name', location='json')
    post_parser_copy.add_argument('mem_sz', location='json')

    def get(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/sdm/initshmem"
        r = requests.get(url, data=args)
        return r.text


class JoinShmem(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('name', location='json')

    def get(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/sdm/joinshmem"
        r = requests.get(url, data=args)
        return r.text

class LeaveShmem(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('name', location='json')

    def get(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/sdm/leaveshmem"
        r = requests.get(url, data=args)
        return r.text


class FreeShmem(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('allocation_info', location='json')

    def get(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/sdm/freeshmem"
        r = requests.get(url, data=args)
        return r.text


class LockMem(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('allocation_info', location='json')

    def get(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/sdm/lockmem"
        r = requests.get(url, data=args)
        return r.text


class UnlockMem(Resource):
    post_parser_copy = post_parser.copy()
    post_parser_copy.add_argument('lock_hndl', location='json')

    def get(self):
        args = self.post_parser_copy.parse_args()
        ipAddress = args.ipAddress
        port = args.port
        del args['port']
        del args['ipAddress']
        url = "http://"+ipAddress+":"+port+"/api/sdm/unlockmem"
        r = requests.get(url, data=args)
        return r.text

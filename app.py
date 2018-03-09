from flask import Flask
import flask_restful
from resources.Switch import Switch
'''Api resource imports'''
from resources.Dbrick import Dbrick, DbrickSwitchOn, DbrickSwitchOff, DbrickIsOn, DbrickPower, DbrickGetBootSource, DbrickSetBootSource, DbrickLinks, DbrickPing
from resources.Dbox import Dbox, DboxTemperature, DboxPower, DboxFanSpeed, DboxPing
from resources.Switch import Switch, SwitchConnectPorts, SwitchDisconnectPort, SwitchPortEndPoint, SwitchPortsInfo, SwitchPowerUtilization
from resources.Memory import AddRemoteMemory, RemoveRemoteMemory, MemoryTest

errors = {
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
    },
    'ConnectionError': {
        'message': "Dbmc-Agent connection cannot be established, check ip and port information",
        'status': 404,
    }
}

app = Flask(__name__)
api = flask_restful.Api(app, errors=errors)

api.add_resource(DbrickSwitchOn, '/api/dbrick/switchon')
api.add_resource(DbrickSwitchOff, '/api/dbrick/switchoff')
api.add_resource(DbrickIsOn, '/api/dbrick/ison')
api.add_resource(Dbrick, '/api/dbrick/info')
api.add_resource(DbrickPower, '/api/dbrick/power')
api.add_resource(DbrickGetBootSource, '/api/dbrick/getbootsource')
api.add_resource(DbrickSetBootSource, '/api/dbrick/setbootsource')
api.add_resource(DbrickLinks, '/api/dbrick/links')
api.add_resource(DbrickPing, '/api/dbrick/ping')

api.add_resource(Dbox, '/api/dbox/info')
api.add_resource(DboxTemperature, '/api/dbox/temperature')
api.add_resource(DboxPower, '/api/dbox/power')
api.add_resource(DboxFanSpeed, '/api/dbox/fanspeed')
api.add_resource(DboxPing, '/api/dbox/ping')

api.add_resource(Switch, '/api/switch/info')
api.add_resource(SwitchConnectPorts, '/api/switch/connectports')
api.add_resource(SwitchDisconnectPort, '/api/switch/disconnectports')
api.add_resource(SwitchPortEndPoint, '/api/switch/portendpoint')
api.add_resource(SwitchPortsInfo, '/api/switch/portsinfo')
api.add_resource(SwitchPowerUtilization, '/api/switch/powerutilization')

api.add_resource(AddRemoteMemory, '/api/memory/addremotememory')
api.add_resource(RemoveRemoteMemory, '/api/memory/removeremotememory')
api.add_resource(MemoryTest, '/api/memory/memorytest')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)

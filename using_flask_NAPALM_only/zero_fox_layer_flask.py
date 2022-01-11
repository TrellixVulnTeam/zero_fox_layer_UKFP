
from flask import Flask, request
from flask_restful import Resource, Api
from napalm.base import get_network_driver
from pydantic import BaseModel
from libs.my_libs import chg_dev_hostname, get_interfaces_info, get_ip_interfaces_info, conf_des_to_interface, create_config_file_to_chg_intf_des
import json

app = Flask(__name__)
api = Api(app)

# *---CISCO DEVICES ONLY---*

##### *---CISCO IOS DEVICES ONLY---*
# -------- ALL GET ENDPOITS --------

class GetDeviceConfig(Resource):
    def get(self):
        return {'message': 'place device config here'}

class GetIntsInfo(Resource):
    def get(self):
        resp = get_interfaces_info()
        return resp

class GetIPIntsInfo(Resource):
    def get(self):
        resp = get_ip_interfaces_info()
        return resp


# -------- END OF ALL GET ENDPOITS --------




# -------- ALL POST ENDPOITS --------
class SendDeviceConfig(Resource):
    def post(self):
        form_data = request.form['new_dev_hostname']
        return {'message sent': form_data}
        chg_dev_hostname

class ConfigDevHostname(Resource):
    def post(self):
        form_data = request.form['new_dev_hostname']
        resp_msg = chg_dev_hostname(form_data)
        return {'response message': resp_msg}

class ConfigIntfDesc(Resource):
    def post(self):
        intf_value_frm = request.form['intf']
        desc_value_frm = request.form['desc']
        resp_msg = conf_des_to_interface(intf_value=intf_value_frm, desc_value=desc_value_frm)
        return {'response message': resp_msg}

# -------- END OF ALL POST ENDPOITS --------



api.add_resource(GetDeviceConfig, '/cisco/ios/get_device_config')
api.add_resource(GetIntsInfo, '/cisco/ios/get_interfaces_info')
api.add_resource(GetIPIntsInfo, '/cisco/ios/get_ip_interfaces_info')
api.add_resource(SendDeviceConfig, '/cisco/ios/send_device_config')
api.add_resource(ConfigDevHostname, '/cisco/ios/chg_dev_hostname')
api.add_resource(ConfigIntfDesc, '/cisco/ios/conf_intf_desc')

###################################
###################################

if __name__ == '__main__':
    app.run(debug=True)

# app.run(debug=True)



# %% [markdown]
# #### import libraries/modules

# %%
from flask import Flask, request
from flask_restful import Resource, Api
from pydantic import BaseModel
from libs.my_libs import chg_dev_hostname
import json

app = Flask(__name__)
api = Api(app)

# *---CISCO DEVICES ONLY---*

##### *---CISCO IOS DEVICES ONLY---*
class GetDeviceConfig(Resource):
    def get(self):
        return {'message': 'place device config here'}

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
        


api.add_resource(GetDeviceConfig, '/cisco/ios/get_device_config')
api.add_resource(SendDeviceConfig, '/cisco/ios/send_device_config')
api.add_resource(ConfigDevHostname, '/cisco/ios/chg_dev_hostname')


       

# %% [markdown]
# #### create the endpoints and their functions
# * endpoints:
#   * **cisco commands**
#   * **juniper commands**
#   * **arista commands**

# %%
# cisco section
##---change hostname of IOS router
##---command
####---hostname [new_hostname]

# class TestClass():
#     def __init__(self, new_dev_name):
#         self.new_dev_name = new_dev_name
    

# class change_device_hostnameModle(BaseModel):
#     texts = list




    # pass
###################################
###################################

if __name__ == '__main__':
    app.run(debug=True)

# app.run(debug=True)



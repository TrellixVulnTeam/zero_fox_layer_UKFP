import re
from string import Template
from typing import Optional
import napalm, os


# *-------- TEMPLATE TO CREATE CUSTOM NAPALM NETWORK DRIVERS --------*
# -------- create a dict to represent the custom driver
# -------- use the dict values as attrbs to instantiate the napalm.get_network_driver() class

# *-------- TEMPLATE TO CREATE ENDPOINT FUNCTION FROM A CUSTOM NAPALM NETWORK DRIVER --------*
# -------- create a dict to represent the custom driver
# -------- use the dict values as attrbs to instantiate the napalm.get_network_driver() class
# -------- use the appropriate method in the custom driver & pass in
# the necessary arguments

# *-------- TEMPLATE TO APPLY CONFIGURATION TO A DEVICE --------*
# -------- create a dict to represent the custom driver
# -------- use the dict values as attrbs to instantiate the
# napalm.get_network_driver() class
# --------use Template module to create a config file to be applied to the
# device
# -------- use the appropriate method in the custom driver to apply
# the config to the device


# create class to config hostname on cisco IOS
#
## use the config file with NAPALM to config new hostname on device
    # #--------DURING DEVELOPMENT ONLY--------#
    # create a NAPALM driver using the mock driver
    # instantiate from that driver and add attrbs to represent a device


    # create a NAPALM driver using the mock driver


ios_driver_args = dict(host='192.168.11.1', uname='cisco', pword='cisco12345')

optional_args = {'secret': 'cisco12345', 'dest_file_system': 'flash:'}

def chg_dev_hostname(new_name):
    # use Template module to create a config file to change the device hostname
    t = Template('hostname $new_namePH')
    command = t.substitute(new_namePH=new_name)

    with open('change_ios_dev_hostname.conf', 'w') as file1:
        entry = f'{command}\n'
        file1.write(entry)
    # entry02 = f'config file created'
    # return entry02

def create_config_file_to_chg_intf_des(func):
    def wrapper(*args, **kwargs):
        
        # use Template module to create a config file to conf intf desc
        t = Template('interface $intfPH \n description $descPH')
        command = t.substitute(intfPH=kwargs['intf_value'], descPH=kwargs['desc_value'])
        # rel_path = '/using_flask_NAPALM_only/libs/test_config.conf'
        # path = os.getcwd() + rel_path
        path = '/home/glitch/Documents/projects/zero_fox_layer/using_flask_NAPALM_only/libs/test_config.conf'
        with open(path, 'w') as file1:
            entry = f'{command}\n'
            file1.write(entry)
        # resp = 'file was created'
        rv = func(*args, **kwargs)
        return rv
    return wrapper
    


def get_interfaces_info():
    # instantiate from the napalm.get_network_driver() class to create a an IOS network driver class called "driver" 
    driver = napalm.get_network_driver('ios')
    
    # instantiate from that driver and add attrbs to represent a device
    with driver(ios_driver_args['host'], ios_driver_args['uname'], ios_driver_args['pword']) as device:
        device.open()
        info = device.get_interfaces() # napalm call no.1
        device.close()
        return info

def get_ip_interfaces_info():
    # instantiate from the napalm.get_network_driver() class to create a an IOS network driver class called "driver" 
    driver = napalm.get_network_driver('ios')
    optional_args = {'secret': 'cisco12345'}
    # instantiate from that driver and add attrbs to represent a device
    with driver(ios_driver_args['host'], ios_driver_args['uname'], ios_driver_args['pword'], optional_args=optional_args) as device:
        device.open()
        info = device.get_interfaces_ip() # napalm call no.1
        device.close()
        return info

@create_config_file_to_chg_intf_des
def conf_des_to_interface(intf_value, desc_value):
    # instantiate from the napalm.get_network_driver() class to create a an IOS network driver class called "driver" 
    driver = napalm.get_network_driver('ios')
    
    # instantiate from that driver and add attrbs to represent a device
    with driver(ios_driver_args['host'], ios_driver_args['uname'], ios_driver_args['pword'], optional_args=optional_args) as device:
        device.open()
        # rel_path = '/using_flask_NAPALM_only/libs/conf_intf_desc.conf'
        # path = os.getcwd() + rel_path
        device.load_merge_candidate(filename='/home/glitch/Documents/projects/zero_fox_layer/using_flask_NAPALM_only/libs/test_config.conf')

        diff = device.compare_config()
        # device.commit_config()

        print(diff)
        device.commit_config()
        device.close()
        # pwd = os.getcwd()
        resp = f'the device was config\'ed & committed'
        return resp

if __name__ == '__main__':
    intf_value_test = 'f0/1'
    desc_value_test = 'mgmt interface'

    conf_des_to_interface(intf_value=intf_value_test, desc_value=desc_value_test)
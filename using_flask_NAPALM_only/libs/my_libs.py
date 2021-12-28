from string import Template
from typing import Optional
import napalm

# create class to config hostname on cisco IOS
## use Template module to create a config file to change the device hostname
## use the config file with NAPALM to config new hostname on device
    # #--------DURING DEVELOPMENT ONLY--------#
    # create a NAPALM driver using the mock driver
    # instantiate from that driver and add attrbs to represent a device


    # create a NAPALM driver using the mock driver




def chg_dev_hostname(new_name):
    # use Template module to create a config file to change the device hostname
    t = Template('hostname $new_namePH')
    command = t.substitute(new_namePH=new_name)

    with open('change_ios_dev_hostname.conf', 'w') as file1:
        entry = f'{command}\n'
        file1.write(entry)
    # entry02 = f'config file created'
    # return entry02
    
    
        # instantiate from that driver and add attrbs to represent a device
    


def get_interfaces_info():
    driver = napalm.get_network_driver('mock')
    with driver('R1', 'cisco', 'cisco12345', optional_args={'path': '/home/glitch/Documents/projects/zero_fox_layer/using_flask_NAPALM_only/napalm_dev_mock_driver_related'}) as device:
        device.open()
        info = device.get_interfaces() # napalm call no.1
        return info

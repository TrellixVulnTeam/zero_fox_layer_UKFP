import napalm



ios_driver_args = dict(host='192.168.11.1', uname='cisco', pword='cisco12345')
driver = napalm.get_network_driver('ios')
    
# instantiate from that driver and add attrbs to represent a device
with driver(ios_driver_args['host'], ios_driver_args['uname'], ios_driver_args['pword'], optional_args={'path': '/home/glitch/Documents/projects/zero_fox_layer/using_flask_NAPALM_only/libs'}) as device:
    print(dir(device.load_replace_candidate(__doc__)))
from string import Template


# create class to config hostname on cisco IOS
## use Template module to create a config file to change the device hostname
## use the config file with NAPALM to config new hostname on device
    
def chg_dev_hostname(new_name):
    # use Template module to create a config file to change the device hostname
    t = Template('hostname $new_namePH')
    command = t.substitute(new_namePH=new_name)

    with open('change_ios_dev_hostname.conf', 'w') as file1:
        entry = f'{command}\n'
        file1.write(entry)
    # entry02 = f'config file created'
    # return entry02

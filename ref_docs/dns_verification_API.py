# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import re, subprocess
from fastapi import FastAPI

# %% [markdown]
# #### //////////////////////////////////////////////////////////////
# #### PERFORM REVERSE DNS LOOKUP ON EACH DEVICE IP ADDRESS BY:
# #### /// - looping thru each line of the file
# %% [markdown]
# - #### open file as "read-only" and create a file object
# - #### loop thru each of the lines in the file
#   - #### while a line is selected:
#     - #### create regex pattern to separate the device ip address from the device hostname
#     - #### using rexex named capture groups:
#       - #### put the device ip address in a group named:
#         - #### dev_ip_addr
#       - #### put the device hostname in a group named:
#         - #### dev_name
#     - #### use the re.search() method to find the matching sub-string
#     - #### save the ip address sub-string to the variable
#       - #### dev_ip_addr
#     - #### save the device hostname sub-string to the variable
#       - #### dev_name
#     - #### using the ip address in **dev_ip_addr** variable, perform a reverse dns lookup
#     - #### extract only the dns name value from the reverse dns lookup
#     - #### separate the dns value into:
#       - #### **device name portion** (named capture group: dev_name) (python var: dev_name_from_dsn_name)
#       - #### **domain name portion** (named capture group: dom_name) (python var: dom_name_from_dsn_name) 
#     - #### compare the device name from the dns server to the device name from file
#     - #### if the two **DO NOT MATCH**:
#         - #### prepare the text in the format:
#           - #### {dns name from server} : {correct dns name}
#     - #### save the text to file:
#       - #### **dns_verification_python_only_result_file-v1.txt**

# %%
app = FastAPI()


@app.get("/verify_dns")
def verify_dns():
    api_return = []
    with open('hostname_to_ip_address_mapping_home_test.txt', 'r') as file2:
        for line in file2:
            pattern1 = '(?P<dev_ip_addr>\d+\.\d+\.\d+\.\d+) (?P<dev_name>.+)'
            match = re.search(pattern1, line)
            dev_ip_addr = match.group('dev_ip_addr') 
            dev_name = match.group('dev_name')



            results = subprocess.run(['nslookup', dev_ip_addr], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output_lines = results.stdout
            pattern = ' = (?P<dsn_name>.+\.net)\.' # replace "pattern" with ATC pattern
            match = re.search(pattern, output_lines)
            dns_name_from_server = match.group('dsn_name')



            pattern3 = '(?P<dev_name>.+)(?P<dom_name>\.1e100\.net)'
            match = re.search(pattern3, dns_name_from_server)
            dev_name_from_dsn_name = match.group('dev_name')
            dom_name_from_dsn_name = match.group('dom_name')



            if dev_name_from_dsn_name != dev_name:
                # bad_dns_name = dns_name_from_server
                good_dns_name = dev_name + dom_name_from_dsn_name
                # good_dns_name = f'{dev_name}{dom_name_from_dsn_name}'
                entry = f'{dns_name_from_server} : {good_dns_name}'
                # entry1 = '************************************\n'

                api_return.append(entry)
                # with open('dns_verification_python_only_result_file-v1.txt', 'a') as file3:
                #     file3.write(entry)
                    # file3.write(entry1)
    return api_return




    
        

# %% [markdown]
# - ## define api endpoint
# - ## define what happens when the api is called with **GET** request
# - ## define the response the api will return
# %% [markdown]
# - #### create an FastAPI application object

# %%


# %% [markdown]
# - #### create an endpoint and define its function
# - #### its function will do the following:
#   - #### call the function ***"verify_dns_func"***
#     - #### this will create a file if there any mis-config'ed dns entries
#   - #### if that file exist, read-in that file & loop thru each line
#   - #### while a line is selected:
#     - #### append the line to a python list
#   - #### return that list as a json object with the key:
#     - #### results

# %%

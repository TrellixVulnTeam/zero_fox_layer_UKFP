# %% [markdown]
# #### import libraries/modules

# %%
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

app = FastAPI()

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

class TestClass():
    def __init__(self, new_dev_name):
        self.new_dev_name = new_dev_name
    

class change_device_hostnameModle(BaseModel):
    texts = list

@app.post("/change_device_hostname")
def change_device_hostname(request: Request):
    # rcv_text = json.load(text.texts)
    # print(f"{rcv_text=}")
    # print(text.texts)
    # test1 = TestClass(new_dev_name=text.texts)
    # print(test1.new_dev_name)
    # return {"message":"message received"}
    return await request.json()



    # pass
###################################
###################################




#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

#Importing the libraries:
#python -m pip install fastapi - To install in Codespace
from fastapi import FastAPI
import uvicorn

app = FastAPI()

#Url to see FastAPI: /docs#

@app.get('/')
def read_root():
    return {'Hello':'BTA Connected Data'}

uvicorn.run(app, host = '0.0.0.0', port="8080")
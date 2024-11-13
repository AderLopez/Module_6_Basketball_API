#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

#Importing the libraries:
#python -m pip install fastapi - To install in Codespace
from fastapi import FastAPI
import uvicorn
from StockFinance import lookup_stock as ls


app = FastAPI()

#Url to see FastAPI: /docs#

@app.get('/')
def read_root():
    return {'Hello':'BTA Connected Data'}

@app.get('/items/{item_id}')
def read_tems(item_id:int,q: str=None):
    string = f'{item_id}*5 = {item_id *5}'
    #Item id is the key and will go:/items/{item_id} - /items/10
    #To use q will be: /items/10?q=This is a message
    return {"item_id":string,"q":q}

#Stock example - static
@app.get('/stocks/{stock_id}')
def read_stock(stock_id: str, q: str=None):
    string = f'This is the price of {stock_id} is 123.12'
    return{'stock_id':string,"q": q}


Stock example - dynamic
@app.get('/stock/{stock_id}')
def read_stock(stock_id:str,q: str=None):
    #querry sql
    #api
    price = ls(stock_id)
    print(price)
    price2 = price['Open']
    print(price2)
    open_list = price['Open'].tolist()
    high_price = price['High'].tolist()
    return {"stock_id":open_list[1:],"high_price":high_price[1:],"q":q}


uvicorn.run(app, host = '0.0.0.0', port="8080")
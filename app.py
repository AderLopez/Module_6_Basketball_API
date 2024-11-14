#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
#Importing the libraries:
#python -m pip install fastapi - To install in Codespace
from flask import Flask,render_template, request
from stock import lookup_stock as ls
import nba 
import urllib.request
import json

#Line of code necessary to change the Path of the templates of HTML since coding in Visual Studio
app = Flask(__name__, template_folder='templates') 

#When running flask, we need to call the python file app.py

#Calling the index.html that will be the home page.
@app.route('/', methods=['POST','GET'])
def Index():
    #nba.all_teams()
    teams_number = nba.all_teams()
    players_number, Highest_country_provider,highest_height,tallest_player = nba.players()
    #current_rate_btc,current_rate_jpy, current_date = Crytocurrency.Bitcoin_rate()
    #return render_template("Module_5_currency.html",Current_date = current_date, Current_rate_BTC = current_rate_btc, Current_rate_JPY = current_rate_jpy )
    return render_template("Dashboard.html", teams_number = teams_number, players_number=players_number,Highest_country_provider=Highest_country_provider,tallest_player=tallest_player,highest_height=highest_height)


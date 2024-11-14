from fastapi import FastAPI
import requests
import pandas as pd
import graph
#import pygal

def check_team(team_id):
    api_url = f"https://api.balldontlie.io/v1/teams/{team_id}"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key


    headers = {"Authorization": f"{api_key}"}

    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    #print(response.json())

    # List to store the responses
    team_list = []

    if response.status_code == 200:
        team_list.append(response.json())



    # Use the key information of the list
    team_name = team_list[0]["data"]["name"]
    team_city = team_list[0]["data"]["city"]
    team_abbreviation = team_list[0]["data"]["abbreviation"]
    print(team_list)
    return team_name, team_city,team_abbreviation




def all_teams():
    api_url = f"https://api.balldontlie.io/v1/teams"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key


    headers = {"Authorization": f"{api_key}"}

    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.json())

    # List to store the responses
    team_list = []

    if response.status_code == 200:
        team_list.append(response.json())
        df = pd.json_normalize(response.json(), 'data')
        #teams_number = df.groupby('id').size()
        teams_number = len(df)
        print("\nTeam count by full name:")
        print(teams_number)
        #print(team_count)
        #team_counts = df.groupby(['city', 'full_name']).size().reset_index(name='team_count')

        #Configuring the information for a dataframe to be displayed when printing:
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 12)
        pd.set_option('display.width', 400) 
        # Count unique team names
        #team_count = df['full_name'].nunique()
        #print("Total number of teams:", team_count)

    # Use the key information of the list
    # team_name = team_list[0]["data"]["name"]
    # team_city = team_list[0]["data"]["city"]
    # team_abbreviation = team_list[0]["data"]["abbreviation"]
    # print(team_list)
    return teams_number#, team_city,team_abbreviation


def players():
    api_url = f"https://api.balldontlie.io/v1/players"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key


    headers = {"Authorization": f"{api_key}"}

    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.json())

    # List to store the responses
    team_list = []

    if response.status_code == 200:
        team_list.append(response.json())
        df = pd.json_normalize(response.json(), 'data')
        #teams_number = df.groupby('id').size()
        players_number = len(df)
        Highest_country_provider =df['country'].value_counts().idxmax()
        print(Highest_country_provider)
        print(players_number)

        #Getting the height in cm:
        df['height_cm'] = df['height'].apply(height_to_cm)
        highest_height = df['height_cm'].max()
        tallest_player_index = df['height_cm'].idxmax()
        tallest_player = df.loc[tallest_player_index, 'first_name']
        #print(team_count)
        #team_counts = df.groupby(['city', 'full_name']).size().reset_index(name='team_count')

        #Configuring the information for a dataframe to be displayed when printing:
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 12)
        pd.set_option('display.width', 400) 
        # Count unique team names
        #team_count = df['full_name'].nunique()
        #print("Total number of teams:", team_count)

    # Use the key information of the list
    # team_name = team_list[0]["data"]["name"]
    # team_city = team_list[0]["data"]["city"]
    # team_abbreviation = team_list[0]["data"]["abbreviation"]
    # print(team_list)

    #Creating graphs:
    name = "Height Distribution"
    values = df['height_cm'] 
    graph.graphs(name,values )


    #Creating graphs:
    name = "Weight Distribution"
    values = df['weight'] 
    print(values)
    graph.graphs(name,values )

    return players_number, Highest_country_provider, highest_height,tallest_player #, team_city,team_abbreviation


#Calculating the height in cm to show the tallest height
def height_to_cm(height):
    feet, inches = map(int, height.split('-'))
    return feet * 30.48 + inches * 2.54
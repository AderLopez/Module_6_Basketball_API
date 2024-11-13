from fastapi import FastAPI
import requests
import uvicorn


def check_team(team_id):
    api_url = f"https://api.balldontlie.io/v1/teams/{team_id}"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key


    headers = {"Authorization": f"{api_key}"}

    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.json())

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

    # Use the key information of the list
    # team_name = team_list[0]["data"]["name"]
    # team_city = team_list[0]["data"]["city"]
    # team_abbreviation = team_list[0]["data"]["abbreviation"]
    # print(team_list)
    return #team_name, team_city,team_abbreviation

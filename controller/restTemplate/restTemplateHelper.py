import requests
from flask import redirect
from urllib.error import HTTPError
import properties

headers = {
    'Authorization': 'Bearer APP_USR-2854379993590279-031220-fd5e9d0b0f8d2ab33bfef6e6382e4b19-307027133'
}

def executeGet(url, endpoint):
    try:
        print(url + endpoint)
        response = requests.get(url + endpoint, headers=headers)
        json = response.json()
        return json
    except HTTPError as e:
        return errorToken()

def errorToken():
    return redirect(properties.user_redirect + properties.auth)

def auth_ml():
    response = requests.get(properties.url_auth + properties.auth)
    html = response.text
    return html



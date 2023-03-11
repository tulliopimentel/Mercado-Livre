import requests
from flask import redirect
from urllib.error import HTTPError
import properties

headers = {
    'Authorization': 'Bearer APP_USR-2854379993590279-031117-862908086ac6c5789c47f6d90e31f802-307027133'
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



import requests
from flask import redirect
from urllib.error import HTTPError
import properties

headers = {
    'Authorization': 'Bearer APP_USR-2854379993590279-031210-91a41b91eb4f4226fd6860bfc2740ee2-307027133'
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



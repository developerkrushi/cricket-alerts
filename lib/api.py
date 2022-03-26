"""This module speaks with Cricket scores API"""
import json
import requests


def fetch_data(api_url):
    """This function calls API and fetch data"""
    try:
        request = requests.get(api_url)
        data = json.loads(request.content.decode())
    except json.decoder.JSONDecodeError:
        msg = "JSON Decode Error. Verify the data string."
    except requests.ConnectionError:
        msg = "Connection Error. Please check your connection."
    except requests.Timeout:
        msg = "Timeout Error!!"
    else:
        if data["livescore"]["current"] == "Data Not Found":
            msg = "Currently No Live Match"
        else:
            msg = f'Match: {data["livescore"]["title"]} \
            \nStatus: {data["livescore"]["update"]} \nCurrent Score: {data["livescore"]["current"]}'

    return msg

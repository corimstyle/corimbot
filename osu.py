import requests
import json
from api_key import api_key


def get_user_info(user):
    payload = {'k': api_key, 'u': user}
    r = requests.get("https://osu.ppy.sh/api/get_user", params=payload)
    return r.json()[0]

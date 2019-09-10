import requests
import json

api_key = "e4768ff59492b8e6008b1dc97db82f59dc63e48e"

def get_user_info(user):
    payload = {'k': api_key, 'u': user}
    r = requests.get("https://osu.ppy.sh/api/get_user", params=payload)
    return r.json()[0]

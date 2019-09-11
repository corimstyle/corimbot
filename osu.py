import requests
import os

# from api_key import api_key // No longer needed

api_key = os.environ.get("OSU_API_KEY")


def get_user_info(user):
    payload = {"k": api_key, "u": user}
    r = requests.get("https://osu.ppy.sh/api/get_user", params=payload)
    return r.json()[0]

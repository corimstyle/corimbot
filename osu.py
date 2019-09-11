import requests
import os

# from api_key import api_key // No longer needed

osu_api_key = os.environ.get("OSU_API_KEY")


def get_user_info(user):
    payload = {"k": osu_api_key, "u": user}
    r = requests.get("https://osu.ppy.sh/api/get_user", params=payload)
    return r.json()[0]

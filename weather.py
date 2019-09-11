import os
from pyowm import OWM

owm_api_key = os.environ.get("OWM_API_KEY")

owm = OWM(owm_api_key)

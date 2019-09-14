import os
from pyowm import OWM

owm_api_key = os.environ.get("OWM_API_KEY")

owm = OWM(owm_api_key)


def forecast(loc):
    fc = owm.three_hours_forecast(loc)
    f = fc.get_forecast()
    print(f.get_weathers())


forecast("san luis obispo")

'''
I used the Sunrise-Sunset API to get the time of sunset in London:
https://sunrise-sunset.org/api

'''

import requests
from datetime import datetime, timedelta

daylight_savings = True 

def str_to_date(time_str):

    time_object = datetime.strptime(time_str, '%H:%M:%S').time()
    date = datetime.combine(datetime.today(), time_object)

    if daylight_savings:
        dls = date + timedelta(hours=1)
        date = datetime.combine(datetime.today(), dls.time())

    return date


def get_sunset_time(lat, long, date) -> datetime:
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&date={date}&formatted=0"

    response = requests.get(url)

    data = response.json()

    try:
        return str_to_date(data['results']['sunset'][11:-6])
    except Exception as e:
        print(f'Error: could not retrieve due to:{data["status"]}, {e}')

import requests
from datetime import datetime


resp = requests.get(url="http://api.open-notify.org/iss-now.json")
print(resp.json()['iss_position']['latitude'])
print(resp.json()['iss_position']['longitude'])
# resp.raise_for_status()
# resp = requests.get(url='https://api.kanye.rest')
# print(resp.json()["quote"])

# DATA FROM: https://www.latlong.net/
# LATITUDE = -14.235004
# LONGITUDE = -51.925282
#
# parameters = {
#     "lat": LATITUDE,
#     "lng": LONGITUDE,
#     # "formatted": 0
# }
#
# rs = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# rs.raise_for_status()
# data = rs.json()
# print(data["results"]["sunrise"])
# print(data["results"]["sunset"])
#
# print(data)

# print(type(datetime.now().hour))

# if 5 > 0 < 10:
#     print("ok")


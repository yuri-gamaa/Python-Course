import requests
import smtplib
from time import sleep
from datetime import datetime

MY_LAT = -14.235004
MY_LONG = -51.925282


def resp_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_params = {
        "lat": float(data["iss_position"]["latitude"]),
        "lgn": float(data["iss_position"]["longitude"]),
        "formatted": 0
    }

    return iss_params


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

time_now = datetime.now()

iss_resp = requests.get(url="https://api.sunrise-sunset.org/json", params=resp_iss())

while True:
    sleep(60)
    try:
        if (MY_LAT + 5 > resp_iss()["lat"] > MY_LAT and
                MY_LONG + 5 > resp_iss()["lgn"] > MY_LONG - 5 and
                18 >= time_now.hour <= 4):
            with smtplib.SMTP('smtp.gmail.com') as mail:
                mail.starttls()
                mail.login(user="aperfilaleatorio@gmail.com", password="SOME_PASSWORD")
                mail.sendmail(from_addr='aperfilaleatorio@gmail.com',
                              to_addrs='aperfilaleatorio@gmail.com',
                              msg=f"Subject:\n\nLook up!")
            print('Done.')
            break

    except requests.exceptions.RequestException:
        print("Trying again.")






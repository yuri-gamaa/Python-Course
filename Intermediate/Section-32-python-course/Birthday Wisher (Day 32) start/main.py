import smtplib as mail_
import datetime as dtime
from random import choice


def send_text(motivational_text):
    email = "aperfilaleatorio@gmail.com"
    passwd = "ygcw lrht cglq tdcl"

    with mail_.SMTP("smtp.gmail.com") as sm:
        sm.starttls()
        sm.login(user=email, password=passwd)
        sm.sendmail(from_addr=email,
                    to_addrs=email,
                    msg=f"Subject:Frase Motivacional\n\n{motivational_text}")


if dtime.datetime.now().weekday() == 1:
    with open('quotes.txt', 'r') as file:
        content = [phrase.strip() for phrase in file]
        phrase = choice(content)
        send_text(phrase)
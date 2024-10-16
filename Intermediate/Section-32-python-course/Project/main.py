##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import json
import smtplib as smt
import datetime as dtime
from random import randint
import pandas


def check(person):
    while True:
        number = randint(1, 3)
        with open('check_letters.json', 'r') as file:
            bd = json.load(file)
            if number not in bd[person]:
                with open(f'letter_templates/letter_{str(number)}.txt', 'r') as file:
                    bd[person].append(number)
                    data = file.read()
                    return data
            else:
                continue


content = pandas.read_csv('birthdays.csv')

for i in range(0, len(content)):
    if dtime.datetime.now().month == content.iloc[i, 3] and dtime.datetime.now().day == content.iloc[i, 4]:

        text = check(content.iloc[i, 0])

        new_text = text.replace('[NAME]', content.iloc[i, 0])

        with smt.SMTP('smtp.gmail.com') as mail:
            mail.starttls()
            mail.login(user='aperfilaleatorio@gmail.com', password='ygcw lrht cglq tdcl')
            mail.sendmail(from_addr='aperfilaleatorio@gmail.com',
                          to_addrs=content.iloc[i, 1],
                          msg=f"Subject:Happy Birthday\n\n{new_text}")

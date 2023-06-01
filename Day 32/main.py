##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv >><<

# 2. Check if today matches a birthday in the birthdays.csv >><<

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas
import random
import os


def check_birthdays():
    birthdays = pandas.read_csv("./day 32/birthdays.csv")
    has_birthday = birthdays[(birthdays["month"] == current_month) & (birthdays["day"] == current_day)]
    return has_birthday


def get_letter(birthday_person):
    name = birthday_person["name"].item()
    letter_list = os.listdir("./day 32/letter_templates")
    letter = random.choice(letter_list)

    with open(f"./day 32/letter_templates/{letter}") as data:
        template = data.read()

    template = template.replace("[NAME]", name)

    return template

def send_email(email_msg):
    email_name = "MYEMAIL"
    email_password = "PASSWORD"
    new_line = "\n"
    connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    connection.starttls()
    connection.login(user=email_name, password=email_password)
    connection.sendmail(
        from_addr=email_name,
        to_addrs="test@test.com",
        msg=f"Subject:Happy Birthday{new_line}{new_line}{email_msg}")
    connection.close()
    ## can not generate app password ###

current_date = dt.datetime.now()
current_day = current_date.day
current_month = current_date.month


birthday_person = check_birthdays()

if birthday_person.empty:
    print("no birthdays")
    #quit()

else:
    email_msg = get_letter(birthday_person)
    print(email_msg)
    # send_email(email_msg)
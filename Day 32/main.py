# import smtplib

# email_name = "MYEMAIL"

# connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
# connection.starttls()
# connection.login(user=email_name, password="PASSWORD_TEST")
# connection.sendmail(from_addr=email_name, to_addrs="test@test.com", msg="Hello Python")
# connection.close()

## can not generate app password

import datetime as dt
import random

with open("./day 32/quotes.txt") as data:
    quotes = data.readlines()

random_quote = random.choice(quotes)
# print(random_quote)
now = dt.datetime.now()
thursday = now.weekday()

if now.weekday() == 3:
    print("Send email")
    print(random_quote)
# print(now)
import requests
from datetime import datetime
import time
import smtplib

MY_LATI = 51.363239
MY_LONG = 6.418240

def iss_part():
    # ISS Part
    url_iss = "http://api.open-notify.org/iss-now.json"

    response_iss = requests.get(url_iss)
    response_iss.raise_for_status()
    iss_json = response_iss.json()

    iss_longitude = float(iss_json["iss_position"]["longitude"])
    iss_latitude = float(iss_json["iss_position"]["latitude"])

    # print(MY_LATI - iss_latitude)
    # print(MY_LONG - iss_longitude)

    if MY_LATI-5 <= iss_latitude <= MY_LATI+5 and MY_LONG-5 <= iss_longitude <= MY_LATI+5:
        return True
    
    return False

def sun_part():
    # Sun Part
    url_sunset = f"https://api.sunrise-sunset.org/json?lat={MY_LATI}&lng=-{MY_LATI}&formatted=0"

    response_sunset = requests.get(url_sunset)
    response_sunset.raise_for_status()
    sunset_json = response_sunset.json()

    sunrise = int(sunset_json["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunset_json["results"]["sunset"].split("T")[1].split(":")[0])

    date_now = datetime.now()
    hour_now = date_now.hour

    if hour_now > sunset or hour_now < sunrise:
        return True

    return False

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
        msg=f"Subject:!!! ISS OVER YOU!!!{new_line}{new_line}{email_msg}")
    connection.close()
    ## can not generate app password ###


while True:
    is_iss_in_air = iss_part()
    # is_iss_in_air = True
    dark = sun_part()
    if dark == True and is_iss_in_air == True:
        print("SEND EMAIL")
        # send_email("WATCH THE SKY")!

    print("ISS is not overhead")
    time.sleep(5) # 60





from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

from dotenv import dotenv_values

config = dotenv_values(".env")
EMAIL = config['EMAIL']
PASSWORD = config['PASSWORD']


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 10)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3590341680&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

driver.get(URL)

# click sing in button
sing_in = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")))
sing_in.click()

# email
email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
email.send_keys(EMAIL)

# password
password_linkedin = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
password_linkedin.send_keys(PASSWORD)

# login button
submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')))
submit_btn.click()

sleep(5)

# driver.quit()


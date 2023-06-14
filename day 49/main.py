
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

from dotenv import dotenv_values

config = dotenv_values(".env")
EMAIL = config['EMAIL']
PASSWORD = config['PASSWORD']


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 30)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3590341680&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

driver.get(URL)

# click sing in button
sing_in = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')))
sing_in.click()

# email
email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
email.send_keys(EMAIL)

# password
password_linkedin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
password_linkedin.send_keys(PASSWORD)

# login button
submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')))
submit_btn.click()

# job list /html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul
jobs_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul')))
jobs = jobs_element.find_elements(By.CSS_SELECTOR, 'li')

sleep(2)

for i in range(1, len(jobs)):
    xpath_job = f"/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div"
    locate_job = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_job)))
    locate_job.click()
    # save the job
    xpath_save_btn = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button'
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_save_btn)))
    save_btn.click()
    sleep(2)
    # follow
    xpath_follow_btn = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/section/section/div[1]/div[1]/button'
    follow_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_follow_btn)))
    driver.execute_script("arguments[0].scrollIntoView(true);", follow_btn)
    sleep(1)
    follow_btn.click()
    sleep(2)
    


sleep(5)

driver.quit()


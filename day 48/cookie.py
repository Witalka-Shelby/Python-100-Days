from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"C:\Users\Witalka\AppData\Local\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)

# timeout = time.time() + 60*5   # 5 minutes from now
purchase = None

while True:
    timeout = time.time() + 2*1   # 10 seconds from now
    money_amount = int(driver.find_element(By.XPATH, '//*[@id="money"]').text)
    cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
    store = driver.find_element(By.XPATH, '//*[@id="store"]')

    upgrades_in_store = store.find_elements(By.CSS_SELECTOR, "div")
    # print(len(upgrades_in_store))
    for i in range(len(upgrades_in_store)):
        id = upgrades_in_store[i].get_attribute("id")
        locked = upgrades_in_store[i].get_attribute("class")
        
        if locked == "grayed":
            continue

        
        try:
            cost = upgrades_in_store[i].find_element(By.CSS_SELECTOR, "b").text.split("-")[1].strip()
            cost = cost.replace(",", "")
        except:
            # print("no , in cost")
            pass

        if money_amount > int(cost):
            purchase = upgrades_in_store[i]
    
    try:
        purchase.click()
        purchase = None
    except:
        print("no upgrades")

    while True:
        cookie.click()
        if time.time() > timeout:
            break
        

driver.quit()
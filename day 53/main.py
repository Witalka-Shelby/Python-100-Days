import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup



from dotenv import dotenv_values

config = dotenv_values(".env")
ZILLOW_URL = config["ZILLOW"]
GOOGLE_FORM = config["GOOGLE_FORM"]

class ZillowBot:
    def __init__(self) -> None:
        options = Options()
        options.binary_location = r"C:\Users\Witalka\AppData\Local\Mozilla Firefox\firefox.exe"

        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_house_prices(self):
        self.driver.get(ZILLOW_URL)
        house_container = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-page-list-container"]')))
        house_element = house_container.find_element(By.CSS_SELECTOR, "div ul")
        houses = house_element.find_elements(By.CSS_SELECTOR, "li")

        houses_dict = {}
        # houses_dict = {0: {'address': '1130 Wyatt St, Clearwater, FL 33756', 'price': '$365,000', 'link': 'https://www.zillow.com/homedetails/1130-Wyatt-St-Clearwater-FL-33756/47192849_zpid/'}, 1: {'address': '1613 N Martin Luther King Jr Ave, Clearwater, FL 33755', 'price': '$350,000', 'link': 'https://www.zillow.com/homedetails/1613-N-Martin-Luther-King-Jr-Ave-Clearwater-FL-33755/47041245_zpid/'}, 2: {'address': '1364 S Evergreen Ave, Clearwater, FL 33756', 'price': '$485,000', 'link': 'https://www.zillow.com/homedetails/1364-S-Evergreen-Ave-Clearwater-FL-33756/47146161_zpid/'}, 3: {'address': '739 Fairwood Ln, Clearwater, FL 33759', 'price': '$379,900', 'link': 'https://www.zillow.com/homedetails/739-Fairwood-Ln-Clearwater-FL-33759/47020993_zpid/'}}
        counter = 0
        for i in range(0 , len(houses)):
            try:
                house_address = houses[i].find_element(By.CSS_SELECTOR, "div div article div div a")
                # print(house_address.text)

                house_price = houses[i].find_element(By.CSS_SELECTOR, "div div article div div div div span")
                # print(house_price.text)

                house_link = house_address.get_attribute("href")
                # print(house_link)

                houses_dict[counter] = {
                    "address": house_address.text,
                    "price": house_price.text,
                    "link": house_link
                }
                counter += 1
            except:
                # print("Not the right element")
                pass

        return houses_dict
    
    def add_into_form(self, houses):
        self.driver.get(GOOGLE_FORM)
    
        for i in range(len(houses)):
            # print(houses[i]["address"])
            # print(houses[i]["price"])
            # print(houses[i]["link"])


            address_form = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")))
            address_form.click()
            address_form.send_keys(houses[i]["address"])

            sleep(1)
            price_form = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")))
            price_form.click()
            price_form.send_keys(houses[i]["price"])

            sleep(1)
            link_form = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")))
            link_form.click()
            link_form.send_keys(houses[i]["link"])

            sleep(1)
            submit_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Y5sE8d > span:nth-child(3) > span:nth-child(1)")))
            submit_btn.click()

            sleep(1)

            submit_another = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".c2gzEf > a:nth-child(1)")))
            submit_another.click()

            sleep(1)


            

if __name__ == "__main__":
    zb = ZillowBot()
    houses = zb.scrape_house_prices()
    zb.add_into_form(houses)
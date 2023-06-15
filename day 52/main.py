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


class InstaBot:
    def __init__(self) -> None:
        options = Options()
        options.binary_location = r"C:\Users\Witalka\AppData\Local\Mozilla Firefox\firefox.exe"

        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 60)

    def follow_people(self):
        # skip day 52 dont want my account banned
        self.driver.get()




















if __name__ == "__main__":
    InstaBot()
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.binary_location = r"C:\Users\Witalka\AppData\Local\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 10)

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(URL)

wiki_number = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")))
# wiki_number.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Community portal").click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("python")
search_bar.send_keys(Keys.ENTER)




 
sleep(5)
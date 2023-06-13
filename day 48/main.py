from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.binary_location = r"C:\Users\Witalka\AppData\Local\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 10)

URL = "https://www.python.org/"
test_dict = {}

driver.get(URL)
events = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")))
all_li = events.find_elements(By.TAG_NAME, "li")

counter = 0
for li in all_li:
    date = li.text.split("\n")[0]
    text = li.text.split("\n")[1]
    test_dict[counter] = {"date": date, "event": text}
    counter += 1

print(test_dict)

driver.quit()
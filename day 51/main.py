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

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

        self.driver = webdriver.Firefox(options=options)
        # actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 60)

        self.down = 150
        self.up = 10

        # self.get_internet_speed()
        self.tweet_post(str(100), str(10))

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        speed_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')))
        speed_button.click()

        sleep(60)

        download_speed = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")))
        upload_speed = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")))
        
        self.tweet_post(download_speed.text, upload_speed.text)
        # print(f"Down: {download_speed.text}")
        # print(f"Up: {upload_speed.text}")

    def tweet_post(self, download_speed, upload_speed):
        url = "https://twitter.com/"
        self.driver.get(url)

        xpath_login = "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]"
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_login)))
        login_button.click()

        username = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-30o5oe")))
        username.click()
        self.driver.implicitly_wait(2)
        username.send_keys(EMAIL)

        self.driver.implicitly_wait(4)

        #click next
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()

        password_t = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-homxoj")))
        password_t.click
        password_t.send_keys(PASSWORD)

        #click log in
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div").click()

        # wait till tweet box
        tweet_box = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html body div#react-root div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 main.css-1dbjc4n.r-1habvwh.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-150rngu.r-16y2uox.r-1wbh5a2.r-rthrr5 div.css-1dbjc4n.r-aqfbo4.r-16y2uox div.css-1dbjc4n.r-1oszu61.r-1niwhzg.r-18u37iz.r-16y2uox.r-1wtj0ep.r-2llsf.r-13qz1uu div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c div.css-1dbjc4n div.css-1dbjc4n.r-14lw9ot.r-184en5c div.css-1dbjc4n div.css-1dbjc4n.r-14lw9ot.r-1h8ys4a div.css-1dbjc4n div.css-1dbjc4n div.css-1dbjc4n.r-ymttw5 div.css-1dbjc4n.r-18u37iz.r-184en5c div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t div.css-1dbjc4n.r-184en5c div.r-42olwf.r-z2wwpe.r-1phboty.r-d045u9.r-6koalj.r-eqz5dr div.css-1dbjc4n.r-16y2uox div.css-1dbjc4n.r-6koalj.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-1bylmt5.r-184en5c div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep.r-136ojw6 div.css-1dbjc4n.r-13qz1uu div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q div.r-1oszu61.r-vqxq0j.r-deolkf.r-6koalj.r-1mlwlqe.r-eqz5dr.r-crgep1.r-ifefl9.r-bcqeeo.r-t60dpp.r-bnwqim.r-417010 div.css-1dbjc4n.r-14lw9ot.r-1yadl64.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-1777fci div.css-1dbjc4n div.css-1dbjc4n.r-1awozwy.r-18u37iz label.css-1dbjc4n.r-1dqbpge.r-13awgt0.r-18u37iz div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 div.css-901oao.r-18jsvk2.r-6koalj.r-37j5jr.r-adyw6z.r-16dba41.r-135wba7.r-bcqeeo.r-qvutc0 div.css-1dbjc4n.r-xoduu5.r-xyw6el.r-mk0yit.r-13qz1uu div.false.draftjs-styles_0 div.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ceczpf.r-1ny4l3l.r-1rnoaur.r-t60dpp.r-1ttztb7 div.DraftEditor-root div.DraftEditor-editorContainer")))
        tweet_box.click()
        tweet_box.send_keys(f'My download speed is {download_speed} and upload {upload_speed}')

        tweet_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.r-l5o3uw:nth-child(4)")))
        #tweet_btn.click()
        print("Tweet")



if __name__ == "__main__":
    InternetSpeedTwitterBot()
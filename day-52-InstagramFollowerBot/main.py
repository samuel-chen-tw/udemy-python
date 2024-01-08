from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


CHROME_DRIVER_PATH = "/Users/chenzhongguang/development/chromedriver"

SIMILAR_ACCOUNT = "cedricgrolet"
USERNAME = "samuel.mycourse@gmail.com"
PASSWORD = "a127275628"

class InstaFollower:

    def __init__(self, driver):
        self.driver = webdriver.Chrome(service=Service(executable_path=driver))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5)

        modal = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(5):
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, '._acan._acap._acas._aj1-._ap30')
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
input("Press Enter to close the browser...")

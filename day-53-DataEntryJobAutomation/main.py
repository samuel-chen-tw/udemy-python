from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import re
from bs4 import BeautifulSoup
import requests

CHROME_DRIVER_PATH = "/Users/chenzhongguang/development/chromedriver"


class DataEntryJob:

    def __init__(self, driver):
        self.driver = webdriver.Chrome(service=Service(executable_path=driver))
        self.all_url = []
        self.all_address = []
        self.all_price = []

    def get_apartment_data(self):
        self.driver.get("https://appbrewery.github.io/Zillow-Clone/")
        time.sleep(2)

        modals = self.driver.find_elements(By.CLASS_NAME, 'ListItem-c11n-8-84-3-StyledListCardWrapper')

        for modal in modals:
            # 處理URL
            url = modal.find_element(By.CLASS_NAME, 'StyledPropertyCardDataArea-anchor').get_attribute('href')
            self.all_url.append(url)
            # 處理價格
            price = modal.find_element(By.CLASS_NAME, 'PropertyCardWrapper__StyledPriceLine').text
            new_price = re.sub(r'[+/].*', '', price)
            self.all_price.append(new_price)
            # 處理地址
            address = modal.find_element(By.TAG_NAME, 'address').text
            new_address = address.replace("| ", "")
            self.all_address.append(new_address)

    # 老師範例
    @staticmethod
    def use_beautiful_soup_to_get_data():
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

        # Use our Zillow-Clone website (instead of Zillow.com)
        response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        # Create a list of all the links on the page using a CSS Selector
        all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
        # Python list comprehension (covered in Day 26)
        all_links = [link["href"] for link in all_link_elements]
        print(f"There are {len(all_links)} links to individual listings in total: \n")
        print(all_links)

        # Create a list of all the addresses on the page using a CSS Selector
        # Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
        all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
        all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
        print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
        print(all_addresses)

        # Create a list of all the prices on the page using a CSS Selector
        # Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
        all_price_elements = soup.select(".PropertyCardWrapper span")
        all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if
                      "$" in price.text]
        print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
        print(all_prices)

    def insert_google_form(self):
        for index in range(len(self.all_address)):
            self.driver.get("https://forms.gle/2DptwFtJoM8nKYuB9")
            time.sleep(2)

            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            prices_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            url_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            address_input.send_keys(self.all_address[index])
            prices_input.send_keys(self.all_price[index])
            url_input.send_keys(self.all_url[index])

            button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            button.click()


bot = DataEntryJob(CHROME_DRIVER_PATH)
bot.get_apartment_data()
bot.insert_google_form()
input("Press Enter to close the browser...")

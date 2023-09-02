from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="/Users/chenzhongguang/development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
nums = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(nums.text)
# nums.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("python")
search.send_keys(Keys.ENTER)


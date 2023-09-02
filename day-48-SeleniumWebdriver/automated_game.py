import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path="/Users/chenzhongguang/development/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_time = 0.1
check_upgrade = click_time * 50

n = 0
while True:
    make_cookies = driver.find_element(By.ID, value='cookie')
    money = int(driver.find_element(By.ID, value='money').text)

    make_cookies.click()  # make cookie by click

    # upgrade the most expensive item on the right site
    item_list = driver.find_elements(By.XPATH, value='//*[@id="store"]/div')
    item_list.pop()  # the last item is empty, so pop up this item
    item_list.reverse()  # we only upgrade the most expensive item, reverse list
    if n % check_upgrade == 0:
        for item in item_list:
            if item:
                cost = int(item.text.split(' - ')[1].split('\n')[0].replace(",", ""))
                if money > cost:
                    item.click()
                    break
    n += 1
    time.sleep(click_time)


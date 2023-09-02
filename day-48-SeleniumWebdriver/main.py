from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/Users/chenzhongguang/development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

# class practice
# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# Use XPATH to get the element
# text = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# print(text.text)

# Use the By.XXX to get the element content
# title = driver.find_element(By.CLASS_NAME, value="widget-title")
# print(title.text)


# 388. Challenge: Scrape website data
events = {}
menu_list = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
for n in range(len(menu_list)):
    content = menu_list[n].text.split("\n")
    events[n] = {
        "time": content[0],
        "name": content[1]
    }
print(events)




# driver.close()
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="/Users/chenzhongguang/development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com")
fName = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
fName.send_keys("Samuel")
lName = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
lName.send_keys("Chen")
email = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email.send_keys("samuel8112@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()


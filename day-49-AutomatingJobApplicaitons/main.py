import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path="/Users/chenzhongguang/development/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3639295852&f_LF=f_AL&keywords=python%20developer&location=台北&refresh=true")

# login button
go_to_login_page = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
go_to_login_page.click()

# login email
email = driver.find_element(By.XPATH, value='//*[@id="username"]')
email.send_keys("samuel811215@gmail.com")

# login password
pwd = driver.find_element(By.XPATH, value='//*[@id="password"]')
pwd.send_keys("a127275628")

# click login
login = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login.click()

time.sleep(5)

# apply job button
apply_job_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button')
apply_job_button.click()

# save job button
# save_job_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
# save_job_button.click()

time.sleep(2)
# phone number
phone = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3639295852-90995746-phoneNumber-nationalNumber"]')
phone.send_keys("0917611749")

next_step = driver.find_element(By.XPATH, value='//*[@id="ember479"]/div/div[2]/form/footer/div[2]/button')
# next_step.click()

# Teacher solution: https://gist.github.com/TheMuellenator/3cc1fdb5f43db6c5d1dd8f773fa4b05c

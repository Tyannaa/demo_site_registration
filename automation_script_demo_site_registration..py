from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random
import time

driver_service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=driver_service)

driver.get('http://dev.bootcamp.store.supersqa.com/')


my_account_link = driver.find_element(By.LINK_TEXT, 'My account')
my_account_link.click()

def generate_random_email():
    username = f"testuser{random.randint(1, 1000)}"
    email = f"{username}@example.com"
    return username, email

username, random_email = generate_random_email()
random_password = 'random_password123'

driver.implicitly_wait(2)

email_input = driver.find_element(By.ID, 'reg_email')
password_input = driver.find_element(By.ID, 'reg_password')

email_input.send_keys(random_email)
password_input.send_keys(random_password)


register_button = driver.find_element(By.NAME, 'register')
register_button.click()

hello_message = driver.find_element(By.XPATH, '//*[contains(text(), "Hello")]')

username_element = driver.find_element(By.XPATH, f'//*[contains(text(), "{username}")]')

if hello_message.is_displayed() and username_element.is_displayed():
    print("Registration successful!!!")
else:
    print("Registration failed!")

driver.quit()

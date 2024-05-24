from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import requests

load_dotenv()

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')

service = Service('/usr/local/bin/chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://intra.42.fr")

usernameField = driver.find_element(By.ID, "username")
passwordField = driver.find_element(By.ID, "password")

usernameField.send_keys(os.getenv("USERNAME"))
passwordField.send_keys(os.getenv("PASSWORD"))
login_button = driver.find_element(By.ID, "kc-login")
login_button.click()

availability = driver.find_element(By.CLASS_NAME, "user-poste-status")
print(availability.text)
host = driver.find_element(By.CLASS_NAME, "user-poste-infos")
print(host.text)

try:
    evals = driver.find_element(By.CLASS_NAME, "project-item-text")
    element_exists = True
except NoSuchElementException:
    element_exists = False

if element_exists:
    message = f"{evals.text} 😀"
    response = requests.post("https://ntfy.coregame.de/intrabot", data=message.encode('utf-8'))

# Close the browser
driver.quit()

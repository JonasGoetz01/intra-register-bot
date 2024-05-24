from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

load_dotenv()

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')

# Set the path to the ChromeDriver
service = Service('/usr/local/bin/chromedriver')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a website
driver.get("https://intra.42.fr")

usernameField = driver.find_element(By.ID, "username")
passwordField = driver.find_element(By.ID, "password")

# Find an element by its name attribute and type something
usernameField.send_keys(os.getenv("USERNAME"))
passwordField.send_keys(os.getenv("PASSWORD"))
login_button = driver.find_element(By.ID, "kc-login")
login_button.click()

# Wait for some time to let the search results load
# time.sleep(5)

# Find a specific element by its tag name and print its text
availability = driver.find_element(By.CLASS_NAME, "user-poste-status")
print(availability.text)
host = driver.find_element(By.CLASS_NAME, "user-poste-infos")
print(host.text)

# Close the browser
driver.quit()

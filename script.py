from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open a website
driver.get("https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=18e6e5cf87aed485fd73aacc6da26dcc0451a85f2bf7d0bc")

usernameField = driver.find_element(By.ID, "username")
passwordField = driver.find_element(By.ID, "password")

# Find an element by its name attribute and type something
usernameField.send_keys(os.getenv(os.getenv("USERNAME")))
passwordField.send_keys(os.getenv(os.getenv("PASSWORD")))
login_button = driver.find_element(By.ID, "kc-login")
login_button.click()

# Wait for some time to let the search results load
time.sleep(5)

# Find a specific element by its tag name and print its text
results = driver.find_element(By.TAG_NAME, "h3")
print(results.text)

# Close the browser
driver.quit()

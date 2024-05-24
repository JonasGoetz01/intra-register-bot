from login import login
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

driver = login()
wait = WebDriverWait(driver, 10)
print(driver.current_url)
# time.sleep(5)
availability = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login")))

print(availability.text)


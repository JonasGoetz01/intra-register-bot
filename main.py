from login import login
from events import Event
from events import registerToEvent
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
registerToEvent(driver)
# time.sleep(5)



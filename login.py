from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
import requests


def login():
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
	try:
		driver.get("https://intra.42.fr")
	except WebDriverException:
		requests.post("https://ntfy.coregame.de/intrabot", data="Intra is not reachable. This bot wont work as expected in the moment.".encode('utf-8'))
		driver.quit()

	try:
		usernameField = driver.find_element(By.ID, "username")
		passwordField = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "kc-login")
	except NoSuchElementException:
		requests.post("https://ntfy.coregame.de/intrabot", data="Login elements not found. This bot doesnt work as expected in the moment".encode('utf-8'))
		driver.quit()
	# Find an element by its name attribute and type something
	usernameField.send_keys(os.getenv("USERNAME"))
	passwordField.send_keys(os.getenv("PASSWORD"))
	login_button.click()

	return driver
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


class Event:
	def __init__(self, name, status):
		self.name = name
		self.status = status
	def isExam(self):
		return self.status == "Exam"


def registerToEvent(driver):
	wait = WebDriverWait(driver, 10)
	events = driver.find_elements(By.CLASS_NAME, "event-button")
	for event in events:
		event.click()
		event_name_element = wait.until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'kind') and text()='Event']/../h4")))
		event_name = event_name_element.text
		print(event_name)
		# if not event.isExam():
		# 	continue
		# event.find_element(By.CLASS_NAME, "btn-primary").click()
		# time.sleep(0.5)
		
	

# availability = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login")))

# print(availability.text)
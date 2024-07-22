import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#driver.get("https://www.redbus.in/")


time.sleep(5)
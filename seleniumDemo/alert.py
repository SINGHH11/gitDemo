import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

name = "Harsh"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,'//input[@id="name"]').send_keys(name)
driver.find_element(By.XPATH,'//input[@id="alertbtn"]').click()

# Switching to Alert :-
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
time.sleep(4)



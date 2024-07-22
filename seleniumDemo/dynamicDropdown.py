import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class ='ui-menu-item'] a")

for i in range (0,len(countries)):
    if countries[i].text == "India":
        countries[i].click()
        break
time.sleep(3)
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

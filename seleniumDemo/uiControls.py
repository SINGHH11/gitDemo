import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# Dynamic Check Boxes :_
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkBoxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
for i in range(0,len(checkBoxes)):
    if checkBoxes[i].get_attribute("id") == "checkBoxOption2":
        checkBoxes[i].click()
        assert checkBoxes[i].is_selected()
        break

# Radio Button :-

radioButton = driver.find_elements(By.XPATH,'//input[@type="radio"]')
radioButton[1].click()

# assertion :-
driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(3)


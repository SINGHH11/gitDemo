import time

import selenium.webdriver.support.select
# Selenium
from selenium import webdriver
# Chrome  Driver
from selenium.webdriver.chrome.service import Service
# Chrome
from selenium.webdriver.common.by import By
# Select Class ( for drop down )
from selenium.webdriver.support.ui import Select

# Launching Chrome

service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# locators :- ID , Name , Class name , Xpath , CSS selector , linkText
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID,"exampleCheck1").click()

# CSS Selector :- tagname[attribute = 'value'] , other methods are ( #id , .className )
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("SINGHH")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1")

# Static Dropdown :-
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
#dropdown.select_by_value()

# XPATH :- //tagname[@sttribute = 'value'] [ Multiple]
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
driver.find_element(By.XPATH,'(//input[@name="name"])[2]').send_keys("hello again")

# Class Name

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print (message)
assert "Success" in message
time.sleep(5)


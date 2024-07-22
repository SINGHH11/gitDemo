import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
# LINK TEXT :-
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# Parent to child using XPATH :-
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
# Parent to child using CSS
driver.find_element(By.CSS_SELECTOR,"form :nth-child(2) input").send_keys("hello@1234")
# CSS ( #ID )
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello@1234")
# XPATH using Text :-
driver.find_element(By.XPATH,"//button[text() = 'Save New Password']").click()

time.sleep(4)
driver.close()
import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

veggieList = []
service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,'(//th[@role="columnheader"])[1]').click()
time.sleep(2)
vegetables = driver.find_elements(By.XPATH,'//tr/td[1]')
for i in range(0,len(vegetables)):
    veggieList.append(vegetables[i].text)

browserSorted = veggieList.copy()
assert browserSorted == veggieList
time.sleep(2)


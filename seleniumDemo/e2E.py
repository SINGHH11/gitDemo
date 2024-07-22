import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,'Shop').click()

# wait = WebDriverWait(driver,10)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.text-center')))

# mobileList = driver.find_elements(By.XPATH,'//app-card')
#for mobile in mobileList:
 #   mobileName = mobile.find_element(By.XPATH,'div/div/h4').text
  #  if mobileName == "Blackberry":
   #     mobile.find_element(By.XPATH,'div/div/button').click()


# Chaining of 'XPATHS' :-

mobileList = driver.find_elements(By.XPATH,'//app-card')
for i in range(0,len(mobileList)):
    mobileName = mobileList[i].find_element(By.XPATH,'div/div/h4').text
    if mobileName == "Blackberry":
        mobileList[i].find_element(By.XPATH,'div/div/button').click()

driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.btn-success').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="country"]').send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.CSS_SELECTOR,'.btn-success').click()
time.sleep(2)
message = driver.find_element(By.CLASS_NAME,'alert-success').text

assert "Success! Thank you!" in message



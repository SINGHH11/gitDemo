import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,'Click Here').click()
time.sleep(3)
totalWindow = driver.window_handles

driver.switch_to.window(totalWindow[1])
Text = driver.find_element(By.XPATH,'//div[@class="example"]').text
driver.close()
driver.switch_to.window(totalWindow[0])
word = driver.find_element(By.XPATH,"//h3[text() = 'Opening a new window']").text
assert word == 'Opening a new window'
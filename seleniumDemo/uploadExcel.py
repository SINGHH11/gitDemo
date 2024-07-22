import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_path = "/Users/harshkumarsingh/Downloads/download.xlsx"
fruit_name = "Apple"
service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"downloadButton").click()

# Edit the excel with updated the value :-

file_input = driver.find_element(By.XPATH,'//input[@type="file"]')
file_input.send_keys(file_path)
toast_locator = (By.XPATH,'//div[text() = "Updated Excel Data Successfully."]')
wait = WebDriverWait(driver,8)
wait.until(EC.presence_of_element_located(toast_locator))
message = driver.find_element(*toast_locator).text
print(message)
time.sleep(2)
price_column = driver.find_element(By.XPATH,'//div[text()="Price"]').get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,'//div[text()="'+fruit_name+'"]/parent::div/parent::div/div[@id="cell-'+price_column+'-undefined"]').text
print(actual_price)
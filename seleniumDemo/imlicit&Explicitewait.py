import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assingment:-
ecpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []


service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,'//input[@type="search"]').send_keys("ber")
time.sleep(4)

results = driver.find_elements(By.XPATH,'//div[@class="products"]/div')
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH,'h4').text)
    result.find_element(By.XPATH,'div/button').click()
assert actualList == ecpectedList

driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
driver.find_element(By.XPATH,'//button[text() = "PROCEED TO CHECKOUT"]').click()

# Sum Validation:-
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for i in range(0,len(prices)):
    sum = sum + int(prices[i].text)

print(sum)
totalSum = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalSum


driver.find_element(By.XPATH,'//input[@placeholder = "Enter promo code"]').send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,'//button[@class="promoBtn"]').click()
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

discountedPrice = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert sum > discountedPrice

print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)





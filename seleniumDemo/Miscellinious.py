import time
import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


service_obj = Service("/Users/harshkumarsingh/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(2)
driver.get_screenshot_as_file("screen.png")
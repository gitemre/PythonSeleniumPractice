from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

s = Service("C:\\Users\\Emre\\Selenium\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']").send_keys("Emre Öztürk")
driver.find_element_by_name("email").send_keys("emreoz-turk@outlook.com")
driver.find_element_by_id("exampleCheck1").click()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Emre\\Selenium\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']").send_keys("Emre Öztürk")
driver.find_element_by_name("email").send_keys("emreoz-turk@outlook.com")
driver.find_element_by_id("exampleCheck1").click()

driver.find_element_by_xpath("//Input[@type='submit']").click()

print(driver.find_element_by_class_name("alert-success").text)

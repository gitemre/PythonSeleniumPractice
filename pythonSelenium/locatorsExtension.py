from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Emre\\Selenium\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("emre33")
driver.find_element_by_css_selector(".password").send_keys("12345")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_name("cancel").click()
print(driver.find_element_by_xpath("form[name='login'] label:nth-child(3)").text)


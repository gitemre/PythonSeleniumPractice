from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Emre\\Selenium\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']").send_keys("Emre Öztürk")
driver.find_element_by_name("email").send_keys("emreoz-turk@outlook.com")
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


driver.find_element_by_xpath("//Input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message

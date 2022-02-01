from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Emre\\Selenium\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()

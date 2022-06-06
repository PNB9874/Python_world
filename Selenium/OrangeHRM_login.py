from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Selenium.readProperties import ReadConfig

URL = ReadConfig.getAppUrl()


service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.get(URL)
print("test")
driver.quit()
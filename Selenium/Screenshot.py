import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(5)
driver.get_screenshot_as_file("E:\PY_Workspace\Python_world\Selenium\Screenshots\Homepage.png")
driver.save_screenshot("E:\PY_Workspace\Python_world\Selenium\Screenshots\saveHomepage.png")




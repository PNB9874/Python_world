"""
ActionChains:
1) Mouse hover
2)right Click
3)Double Cllick
4)Drag and Drop
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="E:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com")

username_textbox = driver.find_element(By.XPATH, "//input[@id='txtUsername']")

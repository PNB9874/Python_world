import time


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

d = webdriver.Chrome(ChromeDriverManager().install())
d.get("http://the-internet.herokuapp.com/javascript_alerts")
d.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(5)
alert = d.switch_to.alert
print(alert.text)

alert.send_keys("Helo")
alert.accept()
time.sleep(10)

print(d.find_element(By.ID,"result").text)
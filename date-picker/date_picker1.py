import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(executable_path="E:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://jqueryui.com/datepicker/?msclkid=80b733bfc44e11eca161f4bdaede9aa1")
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.ID,'datepicker').send_keys("04/25/2022")
# time.sleep(5)


year = "2023"
month = "June"
day = "28"
driver.find_element(By.ID,'datepicker').click()

while True:
   exp_month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
   exp_year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

   if exp_month == month and exp_year==year:
       break;
   else:
       driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
day_list = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in day_list:
    if ele.text == day:
        ele.click()
        break;



time.sleep(5)
#for day in days:



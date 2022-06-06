import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class", params=["GC","FF"])
def setup(request):
    if request.param == "GC":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "FF":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    request.cls,driver = web_driver
    driver.get("https://opensource-demo.orangehrmlive.com/?msclkid=1bcc54a1b56e11ecae17041823baa784")

    yield
    driver.quit()



"""
data driving approach

"""
@pytest.fixture(params=[("Chanti","12345"),("Nagendra","12346")])
def dataLoad(request):
    return request.param


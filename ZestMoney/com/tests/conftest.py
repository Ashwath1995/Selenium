import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = Chrome(executable_path="E:/chromedriver_win32/chromedriver.exe")
    elif browser_name == "firefox":
        driver = Firefox(executable_path="E:/chromedriver_win32/firefox/geckodriver.exe")


    driver.get('https://www.flipkart.com/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action='store', default='firefox')

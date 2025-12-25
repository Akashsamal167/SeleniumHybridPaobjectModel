import pytest
from selenium import webdriver

from utility import ReadConfiguration
from utility.ReadConfiguration import readConfig

@pytest.fixture()
def setup_and_teardown(request):
    browser=ReadConfiguration.readConfig("Basic info","browser")
    driver=None

    if browser == 'chrome':
        driver=webdriver.Chrome()
    elif browser == 'firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Edge()

    driver.maximize_window()

    appurl=ReadConfiguration.readConfig("Basic info","url")
    driver.get(appurl)

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()



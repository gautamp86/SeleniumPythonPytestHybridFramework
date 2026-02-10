import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome")
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox")
        driver.maximize_window()
    else:
        driver = webdriver.Edge()
        print("Launching Edge")
        driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser): # This will get the value from cli/hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

##############PyTest HTML Reports##############
#It is hook for adding envionment info to HTML report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Practice Test Automation"
    config.stash[metadata_key]["Module Name"] = "Practice"
    config.stash[metadata_key]["Tester"] = "Gautam"

#It is hook for delete/modify environment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


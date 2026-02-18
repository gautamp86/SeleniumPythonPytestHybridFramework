import pytest
from selenium import webdriver
from utilities.DriverFactory import DriverFactory
from pytest_metadata.plugin import metadata_key
from utilities.readProperties import ReadConfig


@pytest.fixture
def setup():
    browser = ReadConfig.getBrowser()

    driver = DriverFactory().get_driver(browser)
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


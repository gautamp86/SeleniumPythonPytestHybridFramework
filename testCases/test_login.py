import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.BaseClass import BaseClass


class Test_001_Login(BaseClass):

    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        driver = setup
        driver.get(self.baseUrl)

        try:
            assert driver.title == "Test Login | Practice Test Automation"
            self.logger.info("Home page title test passed")

        except AssertionError:
            self.take_screenshot(driver, "test_homePageTitle")
            self.logger.error("Home page title test failed")
            raise

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        driver = setup
        driver.get(self.baseUrl)

        lp = LoginPage(driver)
        lp.login(self.username, self.password)

        try:
            assert driver.title == "Logged In Successfully | Practice Test Automation"
            self.logger.info("Login test passed")

        except AssertionError:
            self.take_screenshot(driver, "test_login")
            self.logger.error("Login test failed")
            raise

import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***************Test_001_Login***************")
        self.logger.info("***************Verifying home page title***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Test Login | Practice Test Automation":
            assert True
            self.logger.info("***************Home page title test is passed***************")
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.logger.error("***************Home page title test is failed***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************Verifying login test***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        act_title = self.driver.title
        if act_title == "Logged In Successfully | Practice Test Automation":
            self.driver.close()
            assert True
            self.logger.info("***************Login test is passed***************")
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_login.png")
            self.driver.close()
            self.logger.error("***************Login test is failed***************")
            assert False
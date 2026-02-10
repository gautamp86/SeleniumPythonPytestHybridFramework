import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LanguageTablePage import LanguageTablePage
from pageObjects.AddRowPage import AddRowPage
import pytest

class Test_004_LanguageFilter:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_LanguageFiler(self,setup):
        self.logger.info("*************** Test_004_LanguageFilter ***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info("*************** Login is successful ***************")
        self.logger.info("*************** Verifying Language Filter test ***************")
        self.ar = AddRowPage(self.driver)
        self.ar.navigateToPracticePage()
        self.lt = LanguageTablePage(self.driver)
        self.lt.navigateToTestTable()
        self.lt.clickPythonRadioButton()
        languages = self.lt.get_visible_languages()
        for lang in languages:
            if lang == "Python":
                self.logger.info("*************** Successfully verified Python language filter ***************")
                assert True
            else:
                self.driver.save_screenshot("./Screenshots/" + "test_LanguageFilter.png")
                self.logger.info("*************** Language filter is not working ***************")
                assert False

        self.logger.info("*************** End of Language filter test ***************")
        self.logger.info("*************** Completed Test_003_LanguageFilter ***************")







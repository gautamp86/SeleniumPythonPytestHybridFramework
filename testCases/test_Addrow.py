import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddRowPage import AddRowPage
import pytest

class Test_003_AddRow:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddRow(self,setup):
        self.logger.info("*************** Test_003_AddRow ***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info("*************** Login is successful ***************")
        self.logger.info("*************** Verifying Add Row test ***************")
        self.ar = AddRowPage(self.driver)
        self.ar.navigateToPracticePage()
        self.ar.navigateToTestExceptionsPage()
        self.ar.clickAddBtn()
        time.sleep(10)
        confirmation_message = self.ar.displayConfirmationMessage()
        if confirmation_message == "Row 2 was added":
            if self.ar.secondRowDisplayed():
                self.logger.info("*************** Successfully added row 2 ***************")
                assert True
            else:
                self.driver.save_screenshot("./Screenshots/" + "test_AddRow.png")
                self.logger.info("*************** Row 2 was not added ***************")
                assert False

        self.logger.info("*************** End of Add Row test ***************")
        self.logger.info("*************** Completed Test_003_AddRow ***************")


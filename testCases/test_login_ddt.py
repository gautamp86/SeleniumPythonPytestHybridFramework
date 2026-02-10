import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import pytest

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path="TestData/DataLogin.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("***************Test_002_DDT_Login***************")
        self.logger.info("***************Verifying login test***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows = ",self.rows)

        list_status = [] #Empty list variable

        for row in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,'Sheet1',row,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', row, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', row, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Logged In Successfully | Practice Test Automation"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************Passed***************")
                    self.lp.logout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.error("***************Fail***************")
                    self.lp.logout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************Failed****************")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***************Passed******************")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("*************** Login DDT test Passed ***************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************** Login DDT test Failed ***************")
            self.driver.close()
            assert False

        self.logger.info("*************** End of Login DDT test ***************")
        self.logger.info("*************** Completed Test_002_DDT_login ***************")

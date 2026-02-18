from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
from utilities.BaseClass import BaseClass
import pytest


class Test_002_DDT_Login(BaseClass):

    baseUrl = ReadConfig.getApplicationUrl()
    path = "TestData/DataLogin.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("******** Test_002_DDT_Login Started ********")

        driver = setup
        driver.get(self.baseUrl)

        lp = LoginPage(driver)

        rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        self.logger.info(f"Total rows = {rows}")

        list_status = []

        for row in range(2, rows + 1):

            user = ExcelUtils.readData(self.path, "Sheet1", row, 1)
            password = ExcelUtils.readData(self.path, "Sheet1", row, 2)
            exp = ExcelUtils.readData(self.path, "Sheet1", row, 3)

            # ⭐ abstraction (clean login)
            lp.login(user, password)

            act_title = driver.title
            exp_title = "Logged In Successfully | Practice Test Automation"

            if act_title == exp_title and exp == "Pass":
                self.logger.info(f"Row {row} → Passed")
                lp.logout()
                list_status.append("Pass")

            elif act_title != exp_title and exp == "Fail":
                self.logger.info(f"Row {row} → Passed (Negative Test)")
                list_status.append("Pass")

            else:
                self.logger.error(f"Row {row} → Failed")
                self.take_screenshot(driver, f"DDT_Row_{row}")
                list_status.append("Fail")

        # ⭐ Final validation
        assert "Fail" not in list_status, "DDT Login test failed"

        self.logger.info("******** Login DDT test completed ********")

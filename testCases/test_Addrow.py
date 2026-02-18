import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddRowPage import AddRowPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.BaseClass import BaseClass


class Test_003_AddRow(BaseClass):

    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddRow(self, setup):

        self.logger.info("******** Test_003_AddRow Started ********")

        driver = setup
        driver.get(self.baseUrl)

        # ⭐ Login (Abstraction)
        lp = LoginPage(driver)
        lp.login(self.username, self.password)

        self.logger.info("Login successful")

        # ⭐ Add Row flow
        ar = AddRowPage(driver)

        ar.navigate_to_practice_page()
        ar.navigate_to_test_exceptions_page()
        ar.click_add_button()

        # ⭐ No time.sleep needed (handled by BasePage waits)
        confirmation_message = ar.get_confirmation_message()

        try:
            assert confirmation_message == "Row 2 was added"
            assert ar.is_second_row_displayed()

            self.logger.info("Row 2 added successfully")

        except AssertionError:
            self.take_screenshot(driver, "test_AddRow")
            self.logger.error("Add Row test failed")
            raise

        self.logger.info("******** Test_003_AddRow Completed ********")

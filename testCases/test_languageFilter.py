import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.LanguageTablePage import LanguageTablePage
from pageObjects.AddRowPage import AddRowPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.BaseClass import BaseClass


class Test_004_LanguageFilter(BaseClass):

    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_LanguageFilter(self, setup):

        self.logger.info("******** Test_004_LanguageFilter Started ********")

        driver = setup
        driver.get(self.baseUrl)

        # ⭐ Login (Abstraction)
        lp = LoginPage(driver)
        lp.login(self.username, self.password)

        self.logger.info("Login successful")

        # ⭐ Navigate to Practice page
        ar = AddRowPage(driver)
        ar.navigate_to_practice_page()

        # ⭐ Language table actions
        lt = LanguageTablePage(driver)
        lt.navigate_to_test_table()
        lt.click_python_radio_button()

        languages = lt.get_visible_languages()

        try:
            # verify all visible languages are Python
            assert all(lang == "Python" for lang in languages)

            self.logger.info("Python language filter verified successfully")

        except AssertionError:
            self.take_screenshot(driver, "test_LanguageFilter")
            self.logger.error("Language filter validation failed")
            raise

        self.logger.info("******** Test_004_LanguageFilter Completed ********")

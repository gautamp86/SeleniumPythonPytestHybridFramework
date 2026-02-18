from selenium import webdriver

class DriverFactory:

    def get_driver(self, browser):

        if browser == "chrome":
            print("Launching chrome")
            return webdriver.Chrome()

        elif browser == "firefox":
            print("Launching firefox")
            return webdriver.Firefox()

        else:
            print("Launching Edge")
            return webdriver.Edge()

import configparser

config = configparser.RawConfigParser()
config.read('Configurations/config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('Test Environment','baseUrl')
        return url

    @staticmethod
    def getBrowser():
        return config.get('Test Environment', "browser")

    @staticmethod
    def getUseremail():
        username = config.get('Test Environment', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Test Environment', 'password')
        return password
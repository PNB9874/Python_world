import configparser

config = configparser.RawConfigParser()
config.read(r"E:\PY_Workspace\Python_world\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getAppUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserID():
        username = config.get('common info', 'Username')
        return username


    @staticmethod
    def userPassword():
        password = config.get('common info', 'Password')
        return password
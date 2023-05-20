import configparser

config = configparser.RawConfigParser()
config.read("../Config/config.ini")

class readConfig:

    @staticmethod
    def getConfig(self,header,key):
        print(config.get(header,key))
        return config.get(header,key)
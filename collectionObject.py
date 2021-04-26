import ast
from walker import Walker
from datetime import datetime
from selenium import webdriver
from database.dataBaseHandler import DataBase
from driver.session.remote.chromeObject import Session
from driver.session.remote.chromeSettings import ChromeSettings,\
    ChromeCapabilities, ChromeFingerprint
from server.browserConfig import EditConfiguration
from walkerApBlog import WalkerBlog


class Operation:
    def __init__(self, values):
        self.values = values
        self.db = DataBase()

    def setPrivate(self, status):
        self.db.changePrivate(self.values['id'], status)

    def changeLastWalk(self):
        currentDate = datetime.now()
        self.db.updateLastWalk(self.values['id'], currentDate)


class Collection(Operation):
    def __init__(self, values):
        super().__init__(values)
        self.values: dict = values
        self.setPrivate(1)
        self.driver: webdriver.Chrome = self.makeDriver()

    def __del__(self):
        self.setPrivate(0)
        self.changeLastWalk()

    def chromeOptions(self):
        optionsChrome = ChromeSettings().options
        optionsChrome['user-agent'] = self.values['user_agent']
        optionsChrome['screen-resolution'] = self.values['screenResolution']
        optionsChrome['profile'] = self.values['name']
        return optionsChrome

    def capabilitiesOptions(self):
        capabilities = ChromeCapabilities().capabilities
        capabilities['skin'] = self.values['screenResolution'].replace(',', 'x')
        capabilities['browserVersion'] = self.values['name']
        return capabilities

    def fingerprintOptions(self):
        fingerprint = ChromeFingerprint().fingerprint
        fingerprint['platform'] = self.values['platform']
        fingerprint['deviceMemory'] = self.values['deviceMemory']
        fingerprint['hardwareConcurrency'] = self.values['hardwareConcurrency']
        fingerprint['webGlHash'] = self.values['webGLHash']
        fingerprint['webGLVendor'] = self.values['webGLVendor']
        fingerprint['CanvasHash'] = ast.literal_eval(self.values['CanvasHash'])
        return fingerprint

    def makeDriver(self):
        options = self.chromeOptions()
        capabilities = self.capabilitiesOptions()
        fingerprint = self.fingerprintOptions()
        config = EditConfiguration(options['profile'])
        status = config.checkName()
        if status is False:
            config.addProfileConfig()
        return Session(options, capabilities, fingerprint).make()

    def case(self):
        walker = Walker(self.driver)
        walker.execute()

        self.driver.quit()
        walkerBlog = WalkerBlog(self.driver)
        walkerBlog.start()

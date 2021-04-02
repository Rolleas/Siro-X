from driver.session.remote.chromeSettings import ChromeSettings,\
    ChromeCapabilities
from driver.session.remote.chromeObject import Session


class Execution:
    def __init__(self):
        self.driver = self.makeDriver()

    def chromeOptions(self):
        optionsChrome = ChromeSettings().options
        optionsChrome['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        optionsChrome['screen-resolution'] = '1920,1080'
        return optionsChrome

    def capabilities(self):
        cap = ChromeCapabilities().capabilities
        return cap

    def makeDriver(self):
        options = self.chromeOptions()
        capabilities = self.capabilities()
        return Session(options, capabilities).make()

    def case(self):
        import time
        time.sleep(5000)


Execution().case()




from driver.session.remote.chromeSettings import ChromeSettings,\
    ChromeCapabilities, ChromeFingerprint
from driver.session.remote.chromeObject import Session


class Execution:
    def __init__(self):
        self.driver = self.makeDriver()

    @staticmethod
    def chromeOptions():
        optionsChrome = ChromeSettings().options
        optionsChrome['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        optionsChrome['screen-resolution'] = '1920,1080'
        return optionsChrome

    @staticmethod
    def capabilities():
        capabilities = ChromeCapabilities().capabilities
        return capabilities

    @staticmethod
    def fingerprintOptions():
        fingerprint = ChromeFingerprint().fingerprint
        fingerprint['platform'] = "MacIntel"
        fingerprint['WebGlHash'] = 0.039248233
        fingerprint['CanvasHash'] = {'r': 2, 'g': -3, 'b': 5, 'a': -3}
        return fingerprint

    def makeDriver(self):
        options = self.chromeOptions()
        capabilities = self.capabilities()
        fingerprint = self.fingerprintOptions()
        return Session(options, capabilities, fingerprint).make()

    def case(self):
        import time
        time.sleep(5000)


Execution().case()




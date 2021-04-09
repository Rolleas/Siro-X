from driver.session.remote.chromeSettings import ChromeSettings,\
    ChromeCapabilities, ChromeFingerprint
from driver.session.remote.chromeObject import Session


class Execution:
    def __init__(self, values):
        self.values = values
        self.driver = self.makeDriver()

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
        fingerprint['WebGlHash'] = self.values['WebGlHash']
        fingerprint['CanvasHash'] = self.values['CanvasHash']
        return fingerprint

    def makeDriver(self):
        options = self.chromeOptions()
        capabilities = self.capabilitiesOptions()
        fingerprint = self.fingerprintOptions()
        return Session(options, capabilities, fingerprint).make()

    def case(self):
        pass




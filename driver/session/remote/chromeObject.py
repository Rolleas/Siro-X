from selenium import webdriver
from driver.extensions.fingerprint.chromeFinger import Fingerprint

class Session:
    def __init__(self, settings: dict, capabilities: dict, fingerprint: dict):
        self.settings = settings
        self.capabilities = capabilities
        self.fingerprint = fingerprint

    def initFingerprint(self):
        fingerprint = Fingerprint(self.fingerprint)
        extensionPath = fingerprint.makeExtension()
        return extensionPath

    def _chromeOptions(self) -> object:
        chromeOptionsDriver = webdriver.ChromeOptions()
        chromeOptionsDriver.add_argument(
            '--disable-blink-features=AutomationControlled')

        if self.settings['screen-resolution'] is not None:
            chromeOptionsDriver.add_argument(
                f'window-size={self.settings["screen-resolution"]}')

        if self.settings['user-agent'] is not None:
            chromeOptionsDriver.add_argument(
                f'user-agent={self.settings["user-agent"]}')
        chromeOptionsDriver.add_extension(self.initFingerprint())
        return chromeOptionsDriver

    def make(self) -> object:
        objectChrome = webdriver.Remote(
            command_executor="http://45.156.22.26:4444/wd/hub",
            options=self._chromeOptions(),
            desired_capabilities=self.capabilities)
        return objectChrome

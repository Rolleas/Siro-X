from selenium import webdriver


class Session:
    settings: dict

    def __init__(self, settings: dict, capabilities: dict, fingerprint: dict):
        self.settings = settings
        self.capabilities = capabilities
        self.fingerprint = fingerprint

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
        return chromeOptionsDriver

    def make(self) -> object:
        objectChrome = webdriver.Remote(
            command_executor="http://45.156.21.139:4444/wd/hub",
            options=self._chromeOptions(),
            desired_capabilities=self.capabilities)
        objectChrome.current_url
        return objectChrome

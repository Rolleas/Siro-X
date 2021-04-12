from selenium import webdriver
from driver.extensions.fingerprint.chromeFinger import Fingerprint


class Session:
    def __init__(self, settings, capabilities, fingerprint):
        """
        Конструктор принимает набор парамметров для настрйки сессии
        шаблоны хранятся в chromeSettings

        :type fingerprint: dict
        :type capabilities: dict
        :type settings: dict
        """
        self.settings = settings
        self.capabilities = capabilities
        self.fingerprint = fingerprint

    def initFingerprint(self):
        """
        Создание объекта расширения для внедрения настроект отпечатка
        в браузер

        :return extensionPath: object
        """
        fingerprint = Fingerprint(self.fingerprint)
        extensionPath = fingerprint.makeExtension()
        return extensionPath

    def _chromeOptions(self) -> object:
        """
        Создание объекта настроект для сессии браузер
        - отключение webdriver = true
        - изменение разрешения экрана
        - установка значения user-agent
        - отключение WebRTC
        - инитиализация Fingerprint extension

        :return chromeOptionsDriver: object
        """
        chromeOptionsDriver = webdriver.ChromeOptions()
        chromeOptionsDriver.add_argument(
            '--disable-blink-features=AutomationControlled')

        if self.settings['screen-resolution'] is not None:
            chromeOptionsDriver.add_argument(
                f'window-size={self.settings["screen-resolution"]}')

        if self.settings['user-agent'] is not None:
            chromeOptionsDriver.add_argument(
                f'user-agent={self.settings["user-agent"]}')
        preferences = {
            "webrtc.ip_handling_policy": "disable_non_proxied_udp",
            "webrtc.multiple_routes_enabled": False,
            "webrtc.nonproxied_udp_enabled": False
        }
        chromeOptionsDriver.add_argument(
            f'user-data-dir=/home/profiles/{self.settings["profile"]}')
        chromeOptionsDriver.add_experimental_option("prefs", preferences)
        chromeOptionsDriver.add_extension(self.initFingerprint())
        return chromeOptionsDriver

    def make(self) -> object:
        """
        Создание сесси с набором настроект
        возвращает объекта сесси для дальнейшего взаимодействия

        :return objectChrome: object
        """
        objectChrome = webdriver.Remote(
            command_executor="http://45.156.22.26:4444/wd/hub",
            options=self._chromeOptions(),
            desired_capabilities=self.capabilities)
        return objectChrome

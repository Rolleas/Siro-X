class ChromeSettingsPattern:
    OPTIONS = {
        'user-agent': None,
        'platform': 'Win32',
        'proxy': None,
        'user-profile': None,
        'screen-resolution': '1920,1080',
    }

    CAPABILITIES = {
        "browserName": "chrome",
        "browserVersion": "89.0",
        "sessionTimeout": "10m",
        "skin": "1920x1080",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }


class ChromeCapabilities:
    def __init__(self):
        self._capabilities = ChromeSettingsPattern.CAPABILITIES.copy()

    @property
    def capabilities(self) -> dict:
        return self._capabilities

    def set_capabilities(self, name, value):
        if name not in self._capabilities:
            raise ValueError("can't be used")
        else:
            self._capabilities[name] = value


class ChromeSettings:
    def __init__(self):
        self._options = ChromeSettingsPattern.OPTIONS.copy()

    @property
    def options(self) -> dict:
        return self._options

    def set_argument(self, name, value):
        if name not in self._options:
            raise ValueError('cannot be used')
        else:
            self._options[name] = value

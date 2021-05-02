import json
import os


class EditConfiguration:
    _configPath = r'/root/.aerokube/selenoid/browsers.json'
    _command = 'sh /home/rolles/server/Siro-X/server/reload.sh'

    def __init__(self, name):
        """
        Принимает название профиля для добавления в конфигурацию docker
        разделяет доступ к профилям между контейнерами
        :param name: str
        """
        self.name = name

    def _loadFile(self):
        """
        Чтение файла конфигураций
        :return data: str
        """
        with open(self._configPath, 'r') as file:
            data = file.read()
        return data

    def _writeFile(self, data):
        """
        Записывает изменения в файл конфигураций
        :param data: dict
        """
        with open(self._configPath, 'w') as file:
            file.writelines(data)

    def _jsonTransformation(self):
        """
        Преобразование str в dict
        :return data: dict
        """
        data = json.loads(self._loadFile())
        return data

    def _jsonSerializer(self, data):
        """
        Сериализация dict в json и последующая запись в файл
        :param data: dict
        """
        data = json.dumps(data)
        self._writeFile(data)

    def checkName(self):
        data = self._jsonTransformation()
        for element in data['chrome']['versions']:
            if element == self.name:
                return True
        else:
            return False

    def addProfileConfig(self):
        """
        Добавление конфигурации в dict
        """
        data = self._jsonTransformation()
        image = {
            "image": "selenoid/chrome:89.0",
            "port": "4444",
            "volumes": [
                f"/home/profiles/{self.name}:/home/profiles/{self.name}"],
            "path": "/"
        }
        data['chrome']['versions'][self.name] = image
        self._jsonSerializer(data)

        # Перезапуск серверной части для применения конфигурации
        os.system(self._command)
        try:
            os.system(f'mkdir /home/profiles/{self.name}')
            os.system(f'chmod 777 /home/profiles/{self.name}')
        except:
            pass
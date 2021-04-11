import random
from pathlib import Path
from database.dataBaseHandler import DataBase
from server.browserConfig import EditConfiguration


class ProfileGenerator:
    __base_dir = Path(__file__).resolve().parent.parent

    @staticmethod
    def canvasHashGenerator():
        hash = {"r": random.randint(-100, 100), "g": random.randint(-100, 100),
                "b": random.randint(-100, 100), "a": random.randint(-100, 100)}
        return hash

    @staticmethod
    def webGLHash():
        return random.uniform(0.9, 0)

    @staticmethod
    def name():
        db = DataBase()
        string = 'qwertyuiopasdfghjklzxcvbnm'
        name = ''
        while True:
            for _ in range(20):
                name += random.choice(string)
            if db.checkName(name) == ():
                del string, db
                return name

    @staticmethod
    def hardware():
        setNumbers = [number for number in range(2, 32, 2)]
        number = random.choice(setNumbers)
        del setNumbers
        return number

    def webGLVendor(self):
        with open(f'{self.__base_dir}/generator/data/gpu.txt', 'r') as file:
            values = file.read().split('\n')
        return random.choice(values)

    def screens(self):
        with open(f'{self.__base_dir}/generator/data/screens.txt', 'r') as file:
            values = file.read().split('\n')
        return random.choice(values)

    @staticmethod
    def userAgent():
        agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.27 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.20 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.22 Safari/537.36']
        agent = random.choice(agents)
        del agents
        return agent

    def make(self, server):
        profile = {'name': self.name(),
                   'user_agent': self.userAgent(),
                   'screenResolution': self.screens(),
                   'platform': 'Win32',
                   'deviceMemory': self.hardware(),
                   'hardwareConcurrency': self.hardware(),
                   'webGLHash': self.webGLHash(),
                   'webGLVendor': self.webGLVendor(),
                   'CanvasHash': self.canvasHashGenerator(),
                   'server': server}
        db = DataBase()
        db.addProfile(profile)
        del db

        config = EditConfiguration(profile['name'])
        config.addProfileConfig()

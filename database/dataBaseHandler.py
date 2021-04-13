import pymysql
from pymysql import Error as pymysqlError


def DataBaseDecorate(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        args[0].connections.commit()
        return value

    return wrapper


class Connection:
    connections = None
    cursor = None

    def __init__(self):
        self.connections = self.connect()
        self.cursor = self.connections.cursor()

    def __del__(self):
        try:
            self.connections.close()
        except pymysqlError:
            pass

    @staticmethod
    def connect():
        connection = pymysql.connect(host='csgoapblog.beget.tech',
                                     user='csgoapblog_sirox',
                                     password='Deroton88',
                                     database='csgoapblog_sirox',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection


class DataBase(Connection):
    def __init__(self):
        super().__init__()

    def catalogProfiles(self, server) -> list:
        sql = f"SELECT * FROM profiles WHERE server = '{server}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    @DataBaseDecorate
    def updateLastWalk(self, id, time):
        sql = f"UPDATE profiles SET lastWalk = '{time}' WHERE id = '{id}'"
        self.cursor.execute(sql)

    @DataBaseDecorate
    def addProfile(self, profile: dict):
        sql = f'INSERT INTO profiles VALUES (' \
              f'"NULL",' \
              f'"{profile["name"]}",' \
              f'"{profile["user_agent"]}",' \
              f'"{profile["screenResolution"]}",' \
              f'"{profile["platform"]}",' \
              f'"{profile["deviceMemory"]}",' \
              f'"{profile["hardwareConcurrency"]}",' \
              f'"{profile["webGLHash"]}",' \
              f'"{profile["webGLVendor"]}",' \
              f'"{str(profile["CanvasHash"])}",' \
              f'"NULL",' \
              f'"{profile["server"]}", "0")'
        self.cursor.execute(sql)

    @DataBaseDecorate
    def changePrivate(self, profileID, private):
        try:
            sql = f"UPDATE profiles SET private = '{private}' " \
                  f"WHERE id = '{profileID}' "
            self.cursor.execute(sql)
        except:
            self.connections = self.connect()
            self.cursor = self.connections.cursor()
            self.changePrivate(profileID, private)

    def checkName(self, name):
        sql = f"SELECT * FROM profiles WHERE name = '{name}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data


class KeywordsDatabase(Connection):
    def __init__(self):
        super().__init__()

    @DataBaseDecorate
    def addKeyword(self, word):
        sql = f"INSERT INTO keywords VALUES('NULL','{word}')"
        self.cursor.execute(sql)

    def checkKeyword(self, word):
        sql = f"SELECT * FROM keywords WHERE request = '{word}'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get(self, idWord):
        sql = f"SELECT * FROM keywords WHERE id = '{idWord}'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def counterRows(self):
        sql = "SELECT count(*) FROM keywords"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

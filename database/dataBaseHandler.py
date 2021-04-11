import pymysql
from pymysql import Error as pymysqlError


def DataBaseDecorate(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        args[0].connections.commit()
        return value

    return wrapper


class DataBase:
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
        sql = f"UPDATE profiles SET private = '{private}' " \
              f"WHERE id = '{profileID}' "
        self.cursor.execute(sql)

    def checkName(self, name):
        sql = f"SELECT * FROM profiles WHERE name = '{name}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

import pymysql
from pymysql import Error as pymysqlError


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

    def DataBaseDecorate(func) -> object:
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            args[0].connections.commit()
            return value
        return wrapper

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
    def addProfile(self, name, user_agent, screenResolution, platform, deviceMemory,
                   hardwareConcurrency, WebGlHash, webGLVendor, CanvasHash, server):
        sql = f"INSERT INTO profiles (id, name, user_agent, screenResolution," \
              f"platform, deviceMemory, hardwareConcurrency, WebGlHash, webGLVendor," \
              f"CanvasHash, lastWalk, server) VALUES('NULL', '{name}', '{user_agent}'," \
              f"'{screenResolution}', '{platform}', '{deviceMemory}'," \
              f"'{hardwareConcurrency}', '{WebGlHash}', {webGLVendor}, " \
              f"'{CanvasHash}', 'NULL', '{server}')"
        self.cursor.execute(sql)

    @DataBaseDecorate
    def changePrivate(self, id, private):
        sql = f"UPDATE profiles SET private = '{private}' WHERE id = '{id}'"
        self.cursor.execute(sql)

#DataBase().addProfile('ad', 'asd', 'asd','asd','asd','asd','asd','asd','asd')
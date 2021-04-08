import pymysql


class DataBase:
    def __init__(self):
        self.connections = self.connect()
        self.cursor = self.connections.cursor()

    @staticmethod
    def connect():
        connection = pymysql.connect(host='localhost',
                                     user='user',
                                     password='passwd',
                                     database='db',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

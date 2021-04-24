import requests
from xml.etree import ElementTree
from database.dataBaseHandler import KeywordsDatabase
import time

class ScrapKeywords:
    response = None

    def sendRequest(self):
        proxies = {
            "http": "http://37.203.243.208:21236",
            "https": "https://37.203.243.208:21236",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.response = requests.get('https://export.yandex.ru/last/last20x.xml',
                                     headers=headers, proxies=proxies)

    def parsXML(self):
        self.sendRequest()
        try:
            tree = ElementTree.fromstring(self.response.content)
            keywords = []
            for element in tree[0]:
                keywords.append(element.text)
            return keywords
        except:
            pass

    def add(self):
        db = KeywordsDatabase()
        keywords = self.parsXML()
        for element in keywords:
            print(element)
            status = db.checkKeyword(element)
            print(status)
            if status == ():
                print(element)
                db.addKeyword(element)
        del db


while True:
    ScrapKeywords().add()
    time.sleep(10)
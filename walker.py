import time
import random
from database.dataBaseHandler import KeywordsDatabase
from driver.additions.input.inputSys import ActionsDriver


class Walker:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionsDriver(driver)

    @staticmethod
    def chooseKeywords():
        database = KeywordsDatabase()
        amountRows = database.counterRows()
        data = database.get(random.randint(1, amountRows[0]['count(*)']))
        del database
        return data[0]['request']

    def inputRequest(self):
        xpath = "//input[@id='text']"
        self.action.input(xpath, self.chooseKeywords(), True)
        time.sleep(random.uniform(0.1, 0.2))

    def chooseResult(self):
        xpath = "//a/div[@class='OrganicTitle-LinkText organic__url-text' and 2]"
        elements = self.driver.find_elements_by_xpath(xpath)
        elements[random.randint(0, len(elements))].click()
        self.action.wait('/a')
        time.sleep(random.uniform(0.3, 1))

    def execute(self):
        self.driver.get('http://yandex.ru')
        for _ in range(random.randint(40, 100)):
            self.inputRequest()
            self.chooseResult()




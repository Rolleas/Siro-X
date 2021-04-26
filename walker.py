import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from database.dataBaseHandler import KeywordsDatabase
from driver.additions.input.inputSys import ActionsDriver


class Walker:
    keyword = None

    def __init__(self, driver):
        self.driver: webdriver.Chrome = driver
        self.action = ActionsDriver(driver)

    def chooseKeywords(self):
        database = KeywordsDatabase()
        amountRows = database.counterRows()
        data = database.get(random.randint(1, amountRows[0]['count(*)']))
        del database
        self.keyword = data[0]['request']

    def inputFirstRequest(self):
        self.chooseKeywords()
        xpath = "//input[@id='text']"
        self.action.input(xpath, self.keyword, True)
        time.sleep(random.uniform(0.1, 0.2))

    def inputRequest(self):
        xpath = "//input[@id='uniq16167648504181']"
        self.chooseKeywords()
        self.action.input(xpath, self.keyword, True)
        time.sleep(random.uniform(0.1, 0.2))

    def clearInput(self):
        xpath = "/html/body/header/div/div/div[3]/form/div[1]/span/span/span"
        inputElement = self.driver.find_elements_by_xpath(xpath)
        inputElement[0].click()

    def setUrlResult(self):
        xpath = "//a/b[1]"
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements

    def chooseResult(self):
        for _ in range(10):
            try:
                xpath = "//a/div[@class='OrganicTitle-LinkText organic__url-text' and 2]"
                elements = self.driver.find_elements_by_xpath(xpath)
                number = random.randint(0, len(elements)-1)
                elements[number].click()
                self.action.wait('/a')
                time.sleep(random.uniform(0.3, 1))
                return self.setUrlResult()[number].text
            except:
                print("Не могу нажать *-* -><-")
                continue

    def changePage(self):
        elements = self.driver.find_elements_by_xpath('//a')
        elements[random.randint(0, len(elements)-1)].click()
        self.action.wait('//a')
        time.sleep(random.uniform(0.3, 1))

    def firstSteps(self):
        self.driver.get('http://yandex.ru')
        self.action.wait("//input[@id='text']")
        self.inputFirstRequest()
        url = self.chooseResult()
        self.action.swapOnChoose(url)
        self.action.scroll()
        time.sleep(random.uniform(1, 5))

    def inputNewRequest(self):
        self.action.swapOnYandexWindow()
        self.clearInput()
        self.inputRequest()

    def newSite(self):
        url = self.chooseResult()
        self.action.swapOnChoose(url)

    def actionsOnSite(self):
        self.action.scroll()
        self.changePage()
        time.sleep(random.uniform(0.3, 1.5))

    def walkingCurrentRequest(self):
        self.action.swapOnYandexWindow()
        self.newSite()

    def execute(self):
        self.firstSteps()
        for _ in range(random.randint(1, 3)):
            for _ in range(random.randint(1, 5)):
                self.walkingCurrentRequest()
                self.actionsOnSite()
            self.inputNewRequest()
        self.action.closeAllWindow()


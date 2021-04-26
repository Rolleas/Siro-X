import time
import random

from selenium import webdriver
from driver.additions.input.inputSys import ActionsDriver


class WalkerBlog:
    def __init__(self, driver):
        self.driver: webdriver.Chrome = driver
        self.action = ActionsDriver(self.driver)

    def inputRequest(self):
        xpath = "//input[@id='uniq16167648504181']"
        self.action.input(xpath, 'csgoapblog', True)
        time.sleep(random.uniform(0.1, 0.2))

    def chooseSite(self):
        xpath = "//a/div[@class='OrganicTitle-LinkText organic__url-text' and 2]"
        elements = self.driver.find_elements_by_xpath(xpath)
        for index, element in enumerate(elements):
            try:
                element.text.index('https://csgoapblog')
                time.sleep(random.uniform(0.9, 2))
                elements[index].click()
                time.sleep(random.uniform(0.9, 2))
                return True
            except:
                continue

    def changePage(self):
        elements = self.driver.find_elements_by_xpath('//a')
        elements[random.randint(0, len(elements)-1)].click()
        self.action.wait('//a')
        time.sleep(random.uniform(0.3, 2))

    def switchOnSite(self):
        handles = self.driver.window_handles
        for element in handles:
            self.driver.switch_to_window(element)
            currentUrl = str(self.driver.current_url)
            try:
                currentUrl.index('https://csgoapblog')
                time.sleep(random.uniform(0.9, 2))
                return True
            except ValueError:
                continue

    def start(self):
        self.inputRequest()
        self.chooseSite()
        for _ in range(random.randint(5, 20)):
            try:
                self.changePage()
                self.action.scroll()
                time.sleep(random.uniform(0.9, 3))
            except:
                continue


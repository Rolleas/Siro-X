import time
import random

from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class ActionsDriver:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def wait(self, xpath) -> bool:
        """
        Метод для ожидания загрузки элемента на странице
        также можно использовать для ожидании загрузки страницы
        указав любой тег в кодировке xpath к примеру
        wait('//a') таким образом браузер будет ждать появление
        тегов <a>

        :param xpath: xpath элемента для ожидания
        :return bool: True
        """
        for _ in range(60):
            elements = self.driver.find_elements_by_xpath(xpath)
            if elements is not []:
                return True
            else:
                time.sleep(1)

    def input(self, xpath: str, request: str, enter=False):
        """
        Метод для ввода текста в <input> поля
        позволяет немного приблизить к вводу текста под
        по видом обычного пользователя благодаря
        ожиданиями между вводом символов

        :param xpath: xpath элемента в форме строки
        :param request: текст для ввода
        :param enter: нажимать ли Enter после ввода
        """
        if self.wait(xpath) is True:
            element = self.driver.find_elements_by_xpath(xpath)
            element[0].click()
            for symbol in request:
                element[0].send_keys(symbol)
                time.sleep(random.uniform(0.1, 0.2))
            if enter:
                element[0].send_keys(Keys.RETURN)

    def swapOnYandexWindow(self) -> bool:
        """
        Метод для возвращение на вкладу к сайтом яндекса
        в основном этот метод сделан для walker

        :return True: возвращает когда находит вкладку
        """
        handles = self.driver.window_handles
        for element in handles:
            self.driver.switch_to_window(element)
            currentUrl = str(self.driver.current_url)
            try:
                currentUrl.index('https://yandex')
                time.sleep(random.uniform(0.9, 2))
                return True
            except ValueError:
                continue

    def closeAllWindow(self):
        """
        Закрывает все окна кроме яндекса в основном
        этот метод сделан для walker
        """
        handles = self.driver.window_handles
        for element in handles:
            self.driver.switch_to_window(element)
            currentUrl = str(self.driver.current_url)
            time.sleep(random.uniform(0.3, 1))
            try:
                currentUrl.index('http://yandex')
                continue
            except ValueError:
                self.driver.close()

    def swapOnChoose(self, substring: str) -> bool:
        """
        Когда выбираешь сайт в результата поиска на яндексе
        он открывает сайт в новой вкладке. Просто исчем
        вкладку по подстроке ссылки и переключаемся на нее

        :param substring: хранит домен сайта
        :return True: возвращает когда находит вкладку
        """
        handles = self.driver.window_handles
        for element in handles:
            self.driver.switch_to_window(element)
            currentUrl = str(self.driver.current_url)
            try:
                currentUrl.index(substring)
                time.sleep(random.uniform(0.9, 2))
                return True
            except ValueError:
                continue

    def scroll(self):
        """
        Пока ничего лучше такого скролинга сдедать не удалось

        :return:
        """
        for _ in range(random.randint(1, 5)):
            counter = random.randint(100, 300)
            for pixels in range(counter):
                self.driver.execute_script(f"window.scrollBy(0,{pixels})")
                time.sleep(random.uniform(0.2, 0.1))

            for pixels in range(counter):
                self.driver.execute_script(f"window.scrollBy(0,-{pixels})")
                time.sleep(random.uniform(0.2, 0.1))



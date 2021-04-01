import time


# ==========
# Для применения необходимо инициализировать extension/pointer/makePointer
# ==========
class Pointer:
    def __init__(self, chromeDriver):
        self.chromeDriver = chromeDriver

    # ==========
    # Ожидание сменты адреса страницы
    # ==========
    def waiter(self, currentUrl):
        counter = 0
        changedUrl = self.chromeDriver.current_url
        for i in range(10):
            if changedUrl != currentUrl:
                return True
            else:
                counter += 1
                time.sleep(1)
        if counter >= 10:
            return False

    # ==========
    # Принимает selector элемента на сайте и производит клик на него
    # ==========
    def click(self, cssSelector):
        pass

    # ==========
    # Принимает selector элемента на сайте и производит клик на него
    # с перемещением курсора мыши на элемент
    # ==========
    def moveAndClick(self, cssSelector):
        pass

    # ==========
    # Выбирает любой элемент на странице с тегом <a>
    # переещает курсор к элементу и производит клик
    # ==========
    def moveAndClickToRandomElement(self):
        currentUrl = self.chromeDriver.current_url
        jsCode = "pointer.move_to_random_element_and_click()"
        self.chromeDriver.execute_script(jsCode)
        if self.waiter(currentUrl) is False:
            print("Button not pressed")






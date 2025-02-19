from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BaseOption:
    def __init__(self, browser):
        # Инициализация класса BaseOption с браузером и временем ожидания
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)  # Установка времени ожидания в 5 секунд

    def open_page(self):
        # Открытие главной страницы SBIS
        self.browser.get("https://sbis.ru/")

    def find(self, args):
        # Поиск одного элемента на странице по заданным аргументам
        return self.browser.find_element(*args)

    def finds(self, args):
        # Поиск нескольких элементов на странице по заданным аргументам
        return self.browser.find_elements(*args)

    def click_on_an_element(self, args):
        # Клик на элемент, найденный по заданным аргументам
        self.find(args).click()

    def scroll_to_the_element(self, args):
        # Прокрутка страницы к элементу, найденному по заданным аргументам
        while True:
            element = self.find(args)  # Находим элемент
            ActionChains(self.browser).move_to_element(element).perform()  # Прокручиваем к элементу
            return element  # Возвращаем элемент

    def is_block_displayed(self, block):
        # Проверка, отображается ли блок на странице
        return block.is_displayed()

    def get_current_url(self):
        # Получение текущего URL страницы
        return self.browser.current_url
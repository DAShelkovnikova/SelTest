from selenium.webdriver.support import expected_conditions as ec
from options.option_base import BaseOption


class SecondOption(BaseOption):
    # Инициализация класса SecondOption, наследующего от BaseOption
    def __init__(self, browser):
        super().__init__(browser)  # Вызов конструктора родительского класса

    # Ожидание загрузки страницы с определенным заголовком
    def until_partners_load(self):
        self.wait.until(ec.title_contains("Камчатский край"))

    # Проверка, соответствует ли текст региона "Тамбовская обл."
    def region_tambov(self, region):
        return region.text == "Тамбовская обл."

    # Проверка, соответствует ли текст региона "Камчатский край"
    def region_kamchatka(self, new_region):
        return new_region.text == "Камчатский край"

    # Проверка, изменился ли первый партнер
    def new_partners(self, first_partner, new_first_partner):
        return first_partner != new_first_partner

    # Проверка, изменился ли URL
    def url_different(self, url, new_url):
        return url != new_url

    # Проверка, содержит ли новый URL информацию о новом регионе
    def url_contains_new_region(self, new_url):
        return "41-kamchatskij-kraj" in new_url

    # Проверка, содержит ли заголовок страницы информацию о новом регионе
    def title_contains_new_region(self):
        return "Камчатский край" in self.browser.title
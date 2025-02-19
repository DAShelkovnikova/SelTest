from selenium.webdriver.support import expected_conditions as ec
from options.option_base import BaseOption


class FirstOption(BaseOption):

    def __init__(self, browser):
        super().__init__(browser)

    def get_current_page(self):
        return self.browser.current_window_handle

    def select_next_page(self, current_window):
        for window in self.browser.window_handles:
            if current_window != window:
                self.browser.switch_to.window(window)
                break

    def next_page_load(self):
        self.wait.until(ec.title_is("Тензор — IT-компания"))

    def check_url(self):
        return self.get_current_url() == "https://tensor.ru/about"

    def check_the_image_size(self, images):
        height, width = images[0].rect["height"], images[0].rect["width"]
        return all(image.rect["height"] == height and image.rect["width"] == width for image in images[1:])
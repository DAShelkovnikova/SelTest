import requests
import os
from options.option_base import BaseOption


class ThirdOption(BaseOption):

    def __init__(self, browser):
        super().__init__(browser)  # Инициализация родительского класса

    def get_info_from_link(self, links):
        # Проходим по всем ссылкам и ищем подходящие
        for link in links:
            href = link.get_attribute("href")  # Получаем атрибут href
            if href and href.endswith(".exe") and "plugin" in href:  # Проверяем условия
                download_url = href  # Сохраняем URL для загрузки
                filename = os.path.basename(href)  # Извлекаем имя файла из URL
                size_text = link.text.split()[2]  # Получаем текст размера файла
                return download_url, filename, size_text  # Возвращаем сразу, чтобы избежать лишнего цикла
        return None, None, None  # Если ничего не найдено, возвращаем None

    def get_path(self):
        # Возвращаем путь к директории для сохранения файлов
        return os.path.join("files")  # Используем os.path.join для кросс-платформенной совместимости

    def download(self, url, filename, path):
        # Создаем директорию, если она не существует
        if not os.path.exists(path):
            os.makedirs(path)  # Создаем директорию

        response = requests.get(url, stream=True)  # Получаем ответ от сервера
        file_path = os.path.join(path, filename)  # Формируем полный путь к файлу

        with open(file_path, "wb") as exe_file:  # Открываем файл для записи в бинарном режиме
            for chunk in response.iter_content(chunk_size=8192):  # Указываем размер чанка для оптимизации
                exe_file.write(chunk)  # Записываем данные в файл

    def get_real_size(self, path, filename):
        # Получаем размер файла в мегабайтах
        size = os.path.getsize(os.path.join(path, filename)) / (1024 * 1024)  # Переводим в МБ
        return format(size, ".2f")  # Форматируем размер до двух знаков после запятой

    def file_exist(self, path, filename):
        # Проверяем, существует ли файл
        return os.path.isfile(os.path.join(path, filename))  # Возвращаем True или False

    def sizes_equal(self, expected_size, actual_size):
        # Сравниваем ожидаемый и фактический размер
        return expected_size == actual_size  # Возвращаем результат сравнения
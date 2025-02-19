from selenium.webdriver.common.by import By
from conftest import logger
from options.option_three import ThirdOption

# Определение селектора для элемента загрузки внизу страницы
footer_download = (By.XPATH, "//*[@id=\"container\"]/div[2]/div[1]/div[3]/div[3]/ul/li[9]/a")
# Определение селектора для всех ссылок на странице
url_finders = (By.TAG_NAME, "a")


def test_third_option(browser):
    third_option = ThirdOption(browser)

    logger.info("Открытие страницы https://sbis.ru/")
    third_option.open_page()  # Открываем главную страницу
    logger.info("Страница успешно открыта")

    logger.info("Скролл до элемента footer_download")
    third_option.scroll_to_the_element(footer_download)  # Скроллим до элемента загрузки
    logger.info("Скролл прошел успешно")

    logger.info("Поиск и клик по элементу footer_download")
    third_option.click_on_an_element(footer_download)  # Кликаем на элемент загрузки
    logger.info("Поиск и клик прошли успешно")

    logger.info("Поиск всех url")
    links = third_option.finds(url_finders)  # Находим все ссылки на странице
    logger.info("Поиск прошел успешно")

    logger.info("Получение url, имени файла и размера файла со страницы")
    url, filename, size_on_site = third_option.get_info_from_link(links)  # Получаем информацию о файле
    logger.info("Получение url, имени файла и размера пройдено успешно")

    logger.info("Получение пути сохранения")
    path = third_option.get_path()  # Получаем путь для сохранения файла
    logger.info("Путь получен успешно")

    logger.info("Скачивание файла с сайта")
    third_option.download(url, filename, path)  # Скачиваем файл
    logger.info("Скачивание прошло успешно")

    logger.info("Проверка на то что файл скачался")
    assert third_option.file_exist(path, filename)  # Проверяем, что файл существует
    logger.info("Проверка прошла успешно")

    logger.info("Получение настоящего размера файла на компьютере")
    real_size = third_option.get_real_size(path, filename)  # Получаем размер файла на компьютере
    logger.info("Размер файла с компьютера получен")

    logger.info("Сравнение размера файла с сайта с реальным размером на компьютере")
    assert third_option.sizes_equal(size_on_site, real_size)  # Сравниваем размеры файлов
    logger.info("Сравнение прошло успешно")
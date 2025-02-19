from selenium.webdriver.common.by import By
from conftest import logger
from options.option_two import SecondOption

# Определение селекторов для элементов на странице
selectors = {
    "contact_selector_1": (
    By.XPATH, "//*[@id=\"wasaby-content\"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]"),
    "contact_selector_2": (
    By.XPATH, "//*[@id=\"wasaby-content\"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]"),
    "region_selector": (By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span"),
    "first_partner_in_list": (
    By.XPATH, "//*[@id=\"contacts_list\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]"),
    "list_of_partners": (By.NAME, "itemsContainer"),
    "kamchatka_region": (By.XPATH, "//*[@id=\"popup\"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span")
}


def test_second_option(browser):
    second_option = SecondOption(browser)

    logger.info("Открытие страницы https://sbis.ru/")  # Логируем открытие страницы
    second_option.open_page()  # Открываем страницу
    logger.info("Страница успешно открыта")  # Логируем успешное открытие страницы

    # Поиск и клик по контактам
    for contact in ["contact_selector_1", "contact_selector_2"]:
        logger.info(f"Поиск элемента по {contact} и клик")  # Логируем поиск элемента
        second_option.click_on_an_element(selectors[contact])  # Кликаем по элементу
        logger.info("Элемент найден успешно")  # Логируем успешный клик

    # Проверка региона
    logger.info("Поиск элементов по region_selector")  # Логируем поиск региона
    region = second_option.find(selectors["region_selector"])  # Находим элемент региона
    logger.info("Поиск пройден успешно")  # Логируем успешный поиск
    assert second_option.region_tambov(region), "Регион Тамбовская обл."  # Проверяем, что регион соответствует ожиданиям
    logger.info("Проверка пройдена успешно")  # Логируем успешную проверку

    # Получение первого партнера
    logger.info("Поиск элемента по first_partner_in_list")  # Логируем поиск первого партнера
    first_partner = second_option.find(selectors["first_partner_in_list"]).text  # Получаем текст первого партнера
    logger.info("Поиск пройден успешно")  # Логируем успешный поиск

    # Получение текущего URL
    logger.info("Получение текущего url")  # Логируем получение URL
    url = second_option.get_current_url()  # Получаем текущий URL
    logger.info(f"Текущий url получен {url}")  # Логируем полученный URL

    # Поиск блока с партнерами
    logger.info("Поиск блока с партнерами")  # Логируем поиск блока с партнерами
    block_with_partners = second_option.find(selectors["list_of_partners"])  # Находим блок с партнерами
    logger.info("Блок успешно найден")  # Логируем успешный поиск блока
    assert second_option.is_block_displayed(block_with_partners), "Блок с партнерами не отобразился"  # Проверяем отображение блока
    logger.info("Проверка прошла успешно")  # Логируем успешную проверку

    # Выбор региона Камчатка
    for region in ["region_selector", "kamchatka_region"]:
        logger.info(f"Поиск элемента по {region} и клик")  # Логируем поиск региона
        second_option.click_on_an_element(selectors[region])  # Кликаем по региону
        logger.info("Поиск и клик пройдены успешно")  # Логируем успешный клик

    # Ожидание загрузки партнеров
    logger.info("Ожидание пока прогрузится блок с партнерами")  # Логируем ожидание загрузки
    second_option.until_partners_load()  # Ожидаем загрузки партнеров
    logger.info("Ожидание окончено")  # Логируем окончание ожидания

    # Проверка нового региона
    logger.info("Поиск по элементу region_selector")  # Логируем поиск нового региона
    new_region = second_option.find(selectors["region_selector"])  # Находим новый регион
    logger.info("Поиск пройден успешно")  # Логируем успешный поиск
    assert second_option.region_kamchatka(new_region), "Регион не равен Камчатский край"  # Проверяем, что новый регион соответствует ожиданиям
    logger.info("Проверка прошла успешно")  # Логируем успешную проверку

    # Проверка изменения партнеров
    logger.info("Поиск элемента по first_partner_in_list")  # Логируем поиск нового партнера
    new_first_partner = second_option.find(selectors["first_partner_in_list"]).text  # Получаем текст нового партнера
    logger.info("Поиск прошел успешно")  # Логируем успешный поиск
    assert second_option.new_partners(first_partner, new_first_partner), "Партнеры не изменились"  # Проверяем, что партнеры изменились
    logger.info("Проверка прошла успешно")  # Логируем успешную проверку

    # Проверка нового URL
    logger.info("Получение нового url")  # Логируем получение нового URL
    new_url = second_option.get_current_url()  # Получаем новый URL
    logger.info("Новый url получен")  # Логируем полученный новый URL
    assert second_option.url_different(url, new_url), f"Url одинаковые, url = {url}, new_url = {new_url}"  # Проверяем, что URL изменился
    logger.info("Проверка прошла успешно")  # Логируем успешную проверку

    logger.info("Проверка url на содержание нового региона")  # Логируем начало проверки URL
    assert second_option.url_contains_new_region(
        new_url), f"Url не содержит новый регион {new_url}"  # Проверяем, содержит ли URL новый регион
    logger.info("Проверка прошла успешно")  # Логируем успешное завершение проверки URL

    logger.info("Проверка заголовка на содержание нового региона")  # Логируем начало проверки заголовка
    assert second_option.title_contains_new_region(), "Заголовок не содержит новый регион"  # Проверяем, содержит ли заголовок новый регион
    logger.info("Проверка прошла успешно")  # Логируем успешное завершение проверки заголовка
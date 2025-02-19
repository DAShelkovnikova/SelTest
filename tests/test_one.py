from selenium.webdriver.common.by import By
from conftest import logger
from options.option_one import FirstOption

# Определение селекторов для элементов на странице
contact_selectors = {
    "contact_1": (By.XPATH, "//*[@id=\"wasaby-content\"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]"),
    "contact_2": (
    By.XPATH, "//*[@id=\"wasaby-content\"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]"),
    "tensor_image": (By.XPATH, "//*[@id=\"contacts_clients\"]/div[1]/div/div/div[2]/div/a"),
    "power_in_peoples": (By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[5]/div/div/div[1]/div"),
    "more_selector": (By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a"),
    "block_working": (By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img"),
    "image_blocks": (By.CLASS_NAME, "tensor_ru-About__block3-image-wrapper")
}

def test_first_option(browser):
    first_option = FirstOption(browser)

    logger.info("Открытие страницы https://sbis.ru/")  # Логируем открытие страницы
    first_option.open_page()  # Открываем главную страницу
    logger.info("Страница успешно открыта")  # Логируем успешное открытие страницы

    for key in ["contact_1", "contact_2", "tensor_image"]:
        logger.info(f"Поиск элемента по {key} и клик")  # Логируем поиск элемента
        first_option.click_on_an_element(contact_selectors[key])  # Кликаем на элемент
        logger.info("Элемент найден успешно")  # Логируем успешный клик

    logger.info("Получение информации о текущей странице")  # Логируем получение информации о странице
    current_window = first_option.get_current_page()  # Получаем текущую страницу
    logger.info("Информация о текущей странице получена")  # Логируем успешное получение информации

    logger.info("Выбор следующей страницы")  # Логируем выбор следующей страницы
    first_option.select_next_page(current_window)  # Выбираем следующую страницу
    logger.info("Следующая страница выбрано")  # Логируем успешный выбор

    logger.info("Ожидание когда следующая страница загрузится")  # Логируем ожидание загрузки страницы
    first_option.next_page_load()  # Ожидаем загрузку следующей страницы
    logger.info("Страница загрузилась")  # Логируем успешную загрузку страницы

    logger.info("Скролл до элемента Сила в людях")  # Логируем скролл до элемента
    block_power_in_peoples = first_option.scroll_to_the_element(contact_selectors["power_in_peoples"])  # Скроллим до элемента
    logger.info("Скролл прошел успешно")  # Логируем успешный скролл

    logger.info("Проверка блока на отображение")  # Логируем проверку отображения блока
    assert first_option.is_block_displayed(block_power_in_peoples), "Блок \"Сила в людях\" не отображен"  # Проверяем отображение блока
    logger.info("Блок отобразился успешно")  # Логируем успешное отображение блока

    logger.info(f"Поиск элемента по more_selector и клик")  # Логируем поиск элемента more_selector
    first_option.click_on_an_element(contact_selectors["more_selector"])  # Кликаем на элемент
    logger.info("Элемент найден и нажат")  # Логируем успешный клик

    logger.info("Проверка на url")  # Логируем проверку URL
    assert first_option.check_url(), "Url не равен https://tensor.ru/about"  # Проверяем соответствие URL
    logger.info("Проверка пройдена успешно")  # Логируем успешную проверку

    logger.info("Скролл до элемента Работаем")  # Логируем скролл до элемента "Работаем"
    first_option.scroll_to_the_element(contact_selectors["block_working"])  # Скроллим до элемента
    logger.info("Скролл прошел успешно")  # Логируем успешный скролл

    logger.info("Поиск элементов по image_blocks")  # Логируем поиск элементов image_blocks
    images = first_option.finds(contact_selectors["image_blocks"])  # Находим элементы
    logger.info("Элементы найдены успешно")  # Логируем успешный поиск элементов

    logger.info("Проверка высоты и ширины у изображений на равность")  # Логируем проверку размеров изображений
    assert first_option.check_the_image_size(images), "Высота и ширина у изображений не равны"  # Проверяем размеры изображений
    logger.info("Проверка прошла успешно")  # Логируем успешную проверку
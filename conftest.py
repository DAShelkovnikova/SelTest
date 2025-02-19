import logging
from selenium import webdriver
import pytest

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO)
    format="%(asctime)s - %(levelname)s %(message)s",  # Формат сообщения
    handlers=[logging.StreamHandler()]  # Обработчик для вывода в консоль
)

logger = logging.getLogger(__name__)  # Получение логгера для текущего модуля

@pytest.fixture()  # Декоратор для создания фикстуры в pytest
def browser():
    logger.info("Инициализация драйвера")  # Логирование начала инициализации драйвера
    with webdriver.Chrome() as chrome_browser:  # Инициализация Chrome драйвера
        chrome_browser.implicitly_wait(5)  # Установка неявного ожидания в 5 секунд
        yield chrome_browser  # Возврат драйвера для использования в тестах
    logger.info("Закрытие драйвера")  # Логирование закрытия драйвера

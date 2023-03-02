from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class SeleniumBase:
    """
    Описывает общие методы работы selenium.webdrivewer с web элементами.
    1. для упрощения рефракторинга используется аннотация типов;
    2. переменные используемые внутри класса инкапсулировать как __private;
    3. Будем ждать 10 секунд до того, как WebDriverWait вызовет исключение TimeoutException
                           (если найдет элемент за 10 секунд, то вернет его)
    spec. expected_conditions https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
    """

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 30)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME}
        return locating[find_by]

    # Ожидание проверки того, что элемент присутствует на DOM страницы и виден. Возвращает WebElement.
    def is_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # Ожидание проверки того, что все элементы присутствуют в DOM страницы и видны.
    def are_visible(self, find_by: str, locator: str, locator_name=None) -> list[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # Следующие два условия подтверждают,что элемент появляется,и переданные параметры являются локаторами типа кортежа
    # Один будет проходить до тех пор, пока загружен один элемент, соответствующий условиям,
    # а другой должен загрузить все элементы, соответствующие условиям.
    def is_present(self, find_by: str, locator: str, locator_name=None) -> bool:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name=None) -> list[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # Следующие два условия подтверждают, что элемент пропадет со страницы
    def is_not_present(self, find_by: str, locator: str, locator_name=None) -> bool:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def to_be_clickable(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

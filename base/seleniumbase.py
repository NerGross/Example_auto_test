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

    def is_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        """visibility_of_element_located - Ожидание проверки того, что элемент присутствует в DOM объекта страница и видна.
        Видимость означает,  что элемент не только отображается но также имеет высоту и ширину, которые больше 0.
        Локатор - используется  для поиска элемента  возвращает WebElement, как только он будет найден и виден"""
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_staleness_of(self, find_by: str, locator: str, locator_name=None) -> bool:
        """is_staleness_of - Подождите, пока элемент больше не будет присоединен к DOM. element — это элемент ожидания.
        Возвращает False, если элемент все еще прикреплен к DOM, в противном случае — true"""
        return self.__wait.until(ec.staleness_of((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    #
    def to_be_clickable(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        """ Ожидание проверки элемента видно и включено, поэтому вы можете щелкнуть его.
        элемент является либо локатором (текстом), либо WebElement"""
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

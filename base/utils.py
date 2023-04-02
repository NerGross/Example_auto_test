from selenium.webdriver.remote.webelement import WebElement
import cx_Oracle
import config


class Utils:
    """
       Описывает общие методы работы.
       """

    # получаем строковый список -> возвращаем строку с разделителем
    @staticmethod
    def join_strings(str_list: list[str]) -> str:
        return ";".join(str_list)

    # получаем список WebElement -> возвращаем строковый список
    @staticmethod
    def get_text_from_webelements(elements) -> list[str]:
        return [element.text for element in elements]

    # получаем список WebElement, искомое название -> возвращаем WebElement
    @staticmethod
    def get_element_by_name(elements: list[WebElement], name: str) -> WebElement:
        name = name.lower()
        for element in elements:
            if element.text.lower().__contains__(name):  # если текстовое представление элемента содержит name
                return element

    # получаем словарь WebElement, искомое название -> возвращаем WebElement
    @staticmethod
    def get_dict_element_by_name(elements: dict[WebElement], name: str) -> WebElement:
        name = name.lower()
        for key, value in elements.items():
            if key.text.lower() == name:
                return value



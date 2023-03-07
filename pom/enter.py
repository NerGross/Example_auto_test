from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase


class Enter(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        # Вход
        self.__auth: str = '//span[text()="{}"]/..//input'
        self.__button: str = '//button[text()="{}"]'
        self.__company: str = '//div[contains(text(),"{}")]'
        # меню
        self.__menu: str = '//p[text()="{}"]'
        self.__drop_down_meaning: str = '//span[text()="{}"]'

    def get_auth(self, name: str) -> WebElement:
        """поле логин/пароль"""
        return self.is_visible('xpath', self.__auth.format(name), 'auth')

    def get_button(self, name: str) -> WebElement:
        """  кнопка видна и кликабельна  """
        return self.to_be_clickable('xpath', self.__button.format(name), 'button')

    def get_not_button(self, name: str) -> bool:
        """ кнопка не видна"""
        return self.is_not_visible('xpath', self.__button.format(name), 'not_button')

    def get_company(self, name: str) -> WebElement:
        """ кнопка видна и имеет вес, поиск с contains (*содежит часть фразы)"""
        return self.is_visible('xpath', self.__company.format(name), 'company')

    def get_not_company(self, name: str) -> bool:
        """ кнопка не видна"""
        return self.is_not_visible('xpath', self.__company.format(name), 'not_company')

    def get_drop_down_meaning(self, name: str) -> WebElement:
        """ проааадает значение найденого элемента выпадающего списка """
        return self.is_visible('xpath', self.__drop_down_meaning.format(name), 'drop_down_meaning')

    def get_not_drop_down_meaning(self, name: str) -> bool:
        """ проааадает значение найденого элемента выпадающего списка """
        return self.is_not_visible('xpath', self.__drop_down_meaning.format(name), 'drop_down_meaning')

    def get_menu(self, name: str) -> WebElement:
        """ кнопка видна и имеет вес, поиск с contains (*содежит часть фразы)"""
        return self.is_visible('xpath', self.__menu.format(name), 'menu')

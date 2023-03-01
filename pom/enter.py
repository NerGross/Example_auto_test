from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase


class Enter(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        # Вход
        self.__login: str = 'input[name="login"]'
        self.__password: str = 'input[name="password"]'
        self.__button_enter: str = 'button[type="submit"]'
        self.__employee_list: str = '/html/body/div[4]/div/div/div/div[1]/div/ul/li[1]'
        self.__menu_item: str = '//p[text()="Объекты страхования"]'
        self.__menu_item_child: str = '//p[text()="Транспортные средства"]'

    # поле логин
    def get_login(self) -> WebElement:
        return self.is_visible('css', self.__login, 'login')

    # поле пароль
    def get_password(self) -> WebElement:
        return self.is_visible('css', self.__password, 'password')

    # кнопка Войти
    def get_button_enter(self) -> WebElement:
        return self.is_visible('css', self.__button_enter, 'button_enter')

    # Выбор компании страхователя
    def get_employee_list(self) -> WebElement:
        return self.is_visible('xpath', self.__employee_list, 'employee_list')

    # меню "Объект страхователя"
    def get_menu_item(self) -> WebElement:
        return self.is_visible('xpath', self.__menu_item, 'menu_item')

    # подменю "Транспортное средство"
    def get_menu_item_child(self) -> WebElement:
        return self.is_visible('xpath', self.__menu_item_child, 'menu_item_child') \
 \
    # проверка о загрузке страницы
    def get_wait_load_dom(self):
        if self.driver.execute_script("return document.readyState") == "complete":
            return True
        else:
            return False

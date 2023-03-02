from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase
from base.utils import Utils


class Vehicle(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        # ТС
        self.__button: str = '//button[text()="{}"]'
        self.__accordion_chapter: str = '//div[text()="{}"]'
        self.__input: str = '//span[text()="{}"]/parent::label//span//input'
        self.__drop_down: str = '//span[text()="{}"]/..//div[@role]'
        self.__drop_down_find: str = '//input[@placeholder="Поиск"]'
        self.__drop_down_meaning: str = '//span[text()="{}"]'
        # не перевести в универсальные
        self.__doc_vehicle_series: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[1]/span[2]/input'
        self.__doc_vehicle_number: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[2]/span[2]/input'
        self.__doc_vehicle_date: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/div/div/div[1]/label/span[1]/input'
        self.__doc_TO_date: str = '//*[@id="vehicle-form"]/div[5]/div[2]/div/div[2]/div/div/div[1]/label/span[1]/input'
        self.__vehicle_journal: str = '//tbody'

        # импорт
        self.__upload: str = 'input[name ="file"]'
        self.__upload_stat: str = '//tr/td[1]'
        self.UPLOAD_STAT = "Успешно"

    # кнопка
    def get_button(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__button.format(name), 'button')

    # проверка о загрузке страницы проверкой доступности кнопки
    def get_wait_load_dom(self, name):
        if self.to_be_clickable('xpath', self.__button.format(name), 'wait_load_dom'):
            return True
        else:
            return False

    # выбор раздела аккардеона
    def get_accordion_chapter(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__accordion_chapter.format(name), 'accordion_chapter')

    # Выбор поля
    def get__input(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__input.format(name), 'input')

    # Выбор выпадающего списка
    def get_drop_down(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__drop_down.format(name), 'drop_down')

    # поиск внутри выпадающего списка
    def get_drop_down_find(self) -> WebElement:
        return self.is_visible('xpath', self.__drop_down_find, 'drop_down_find')

    # выбрать значение найденого элемента выпадающего списка
    def get_drop_down_meaning(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__drop_down_meaning.format(name), 'drop_down_meaning')

    # Серия документа о регистрации
    def get_doc_vehicle_series(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_vehicle_series, 'doc_vehicle_series')

    # номер документа о регистрации
    def get_doc_vehicle_number(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_vehicle_number, 'doc_vehicle_number')

    # дата документа о регистрации
    def get_doc_vehicle_date(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_vehicle_date, 'doc_vehicle_date')

    # дата документа о регистрации
    def get_doc_TO_date(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_TO_date, 'doc_TO_date')

    # Получаем журнал ТС -> список webElement
    def get_vehicle_Journal(self) -> str:
        vehicle_journal = self.are_visible('xpath', self.__vehicle_journal, 'vehicle_journal')
        return Utils.join_strings(Utils.get_text_from_webelements(vehicle_journal))

    # область для загрузки файлов
    def get_upload(self) -> WebElement:
        self.driver.execute_script('document.querySelector("input[name = file]").style.visibility = "visible"')
        self.driver.execute_script('document.querySelector("input[name = file]").style.width = "10px"')
        self.driver.execute_script('document.querySelector("input[name = file]").style.height = "10px"')
        return self.is_visible('css', self.__upload, 'upload')

    # проверка статуса загрузки
    def get_upload_stat(self) -> str:
        return self.is_visible('xpath', self.__upload_stat, 'upload_stat').text

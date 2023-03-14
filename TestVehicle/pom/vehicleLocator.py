from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase
from base.utils import Utils


class VehicleLocator(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        # ТС
        self.__button: str = '//button[text()="{}"]'
        self.__accordion_chapter: str = '//div[text()="{}"]'
        self.__input: str = '//span[text()="{}"]/parent::label//span//input'
        self.__drop_down: str = '//span[text()="{}"]/..//div'
        self.__drop_down_find: str = '//input[contains(@placeholder,"Поиск")]'
        self.__drop_down_meaning: str = '//span[contains(text(),"{}")]'
        # не перевести в универсальные
        self.__doc_vehicle_series: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[1]/span[2]/input'
        self.__doc_vehicle_number: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[2]/span[2]/input'
        self.__doc_vehicle_date: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/div/div/div[1]/label/span[1]/input'
        self.__doc_TO_date: str = '//*[@id="vehicle-form"]/div[5]/div[2]/div/div[2]/div/div/div[1]/label/span[1]/input'
        self.__vehicle_journal: str = '//tbody'

        # импорт
        self.__upload: str = 'input[name ="file"]'
        self.__upload_stat: str = '//tr/td[1]'
        self.__template: str = '/html/body/div[2]/div/div/form/div[3]/div/div/span'
        self.UPLOAD_STAT = "Успешно"

    def get_button(self, name: str) -> WebElement:
        """Кнопка видна и кликабельна """
        return self.to_be_clickable('xpath', self.__button.format(name), 'button')

    def get_not_button(self, name: str) -> bool:
        """Кнопка не видна"""
        return self.is_not_visible('xpath', self.__button.format(name), 'not_button')

    def get_accordion_chapter(self, name: str) -> WebElement:
        """Выбор раздела аккордеона """
        return self.is_visible('xpath', self.__accordion_chapter.format(name), 'accordion_chapter')

    def get__input(self, name: str) -> WebElement:
        """Выбор поля (implicitly_wait)"""
        return self.find_element('xpath', self.__input.format(name))

    def get_drop_down(self, name: str) -> WebElement:
        """Выбор выпадающего списка """
        return self.is_visible('xpath', self.__drop_down.format(name), 'drop_down')

    def get_drop_down_find(self) -> WebElement:
        """Поиск внутри выпадающего списка """
        return self.is_visible('xpath', self.__drop_down_find, 'drop_down_find')

    def get_drop_down_meaning(self, name: str) -> WebElement:
        """Выбрать значение найденного элемента выпадающего списка """
        return self.is_visible('xpath', self.__drop_down_meaning.format(name), 'drop_down_meaning')

    def get_doc_vehicle_series(self) -> WebElement:
        """Серия документа о регистрации """
        return self.is_visible('xpath', self.__doc_vehicle_series, 'doc_vehicle_series')

    def get_doc_vehicle_number(self) -> WebElement:
        """Номер документа о регистрации """
        return self.is_visible('xpath', self.__doc_vehicle_number, 'doc_vehicle_number')

    def get_doc_vehicle_date(self) -> WebElement:
        """Дата документа о регистрации """
        return self.is_visible('xpath', self.__doc_vehicle_date, 'doc_vehicle_date')

    def get_doc_to_date(self) -> WebElement:
        """Дата документа о регистрации """
        return self.is_visible('xpath', self.__doc_TO_date, 'doc_TO_date')

    def get_vehicle_journal(self) -> str:
        """Получаем журнал ТС -> список webElement """
        vehicle_journal = self.are_visible('xpath', self.__vehicle_journal, 'vehicle_journal')
        return Utils.join_strings(Utils.get_text_from_webelements(vehicle_journal))

    def get_upload(self) -> WebElement:
        """Область для загрузки файлов. JS даем области вес и видимость """
        # self.driver.execute_script('document.querySelector("input[name = file]").style.visibility = "visible"')
        # self.driver.execute_script('document.querySelector("input[name = file]").style.width = "10px"')
        # self.driver.execute_script('document.querySelector("input[name = file]").style.height = "10px"')
        return self.find_element('css', self.__upload)

    def get_upload_stat(self) -> str:
        """Проверка статуса загрузки """
        return self.is_visible('xpath', self.__upload_stat, 'upload_stat').text

    def get_template(self) -> WebElement:
        """Шаблон загрузки"""
        return self.is_visible('xpath', self.__template, 'template')

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
        # старые
        self.__doc_type_section: str = '/html/body/div[1]/div/div/main/div/form/div[4]/div[2]/div/div[1]/div[1]/div'
        self.__doc_type: str = '//span[text()="Паспорт ТС"]'
        self.__doc_series: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[1]/span[2]/input'
        self.__doc_number: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[2]/span[2]/input'
        self.__doc_date: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/div/div/div[1]/label/span[1]/input'
        self.__vehicle_Journal: str = '//*[@id="sgb2b"]/div/div/main/div/table'
        # импорт
        self.__button_vehicle_import: str = '//*[@id="sgb2b"]/div/div/div[1]/div[3]/div[1]/button[1]'
        self.__uploader: str = '/html/body/div[2]/div/div/form/div[2]/label/div[1]/span[1]'
        self.__close: str = '/html/body/div[2]/div/div/form/div[4]/button[2]'

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

    # старье

    # открыть спиок документов на ТС
    def get_doc_type_section(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_type_section, 'doc_type_section')

    # выбрать категорию документа на ТС
    def get_doc_type(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_type, 'doc_type')

    # Серия документа о регистрации
    def get_doc_series(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_series, 'doc_series')

    # номер документа о регистрации
    def get_doc_number(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_number, 'doc_number')

    # дата документа о регистрации
    def get_doc_date(self) -> WebElement:
        return self.is_visible('xpath', self.__doc_date, 'doc_date')

    # Получаем журнал ТС -> список webElement
    def get_vehicle_Journal(self) -> list[WebElement]:
        return self.are_visible('xpath', self.__vehicle_Journal, 'vehicle_Journal')

    # Получаем список WebElement ->  возвращаем строку елементов
    def get_vehicle_Journal_text(self) -> str:
        return Utils.join_strings(Utils.get_text_from_webelements(self.get_vehicle_Journal()))

    # область для загрузки файлов
    def get_uploader(self) -> WebElement:
        return self.is_visible('xpath', self.__uploader, 'upload')

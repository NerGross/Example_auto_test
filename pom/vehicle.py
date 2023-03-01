from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase
from base.utils import Utils


class Vehicle(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        # ТС
        self.__button_add_vehicle: str = '//*[@id="sgb2b"]/div/div/div[1]/div[3]/div[1]/button[2]'
        self.__find: str = '//input[@placeholder="Поиск"]'
        self.__accordion_chapter: str = '//div[text()="{0}"]'
        self.__input: str = '//span[contains(text(),"{}")]/parent::label//span//input'
        # старые
        self.__cat_section: str = '//*[@id="vehicle-form"]/div[1]/div[2]/div/div[5]/div[1]/div'
        self.__cat: str = '//span[text()="B"]'
        self.__type_vehicle_section: str = '//*[@id="vehicle-form"]/div[1]/div[2]/div/div[5]/div[2]/div'
        self.__type_vehicle: str = '//span[text()="Легковой"]'
        self.__doc_type_section: str = '/html/body/div[1]/div/div/main/div/form/div[4]/div[2]/div/div[1]/div[1]/div'
        self.__doc_type: str = '//span[text()="Паспорт ТС"]'
        self.__doc_series: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[1]/span[2]/input'
        self.__doc_number: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/label[2]/span[2]/input'
        self.__doc_date: str = '//*[@id="vehicle-form"]/div[4]/div[2]/div/div[2]/div/div/div[1]/label/span[1]/input'
        self.__vehicle_save: str = '//*[@id="vehicle-form"]/div[8]/div/button[1]'
        self.__vehicle_Journal: str = '//*[@id="sgb2b"]/div/div/main/div/table'
        # импорт
        self.__button_vehicle_import: str = '//*[@id="sgb2b"]/div/div/div[1]/div[3]/div[1]/button[1]'
        self.__uploader: str = '/html/body/div[2]/div/div/form/div[2]/label/div[1]/span[1]'
        self.__close: str = '/html/body/div[2]/div/div/form/div[4]/button[2]'

    # кнопка Добавить ТС
    def get_button_add_vehicle(self) -> WebElement:
        return self.is_visible('xpath', self.__button_add_vehicle, 'button_add_vehicle')

    # поиск внутри выпадающего списка
    def get_find(self):
        return self.is_visible('xpath', self.__find, 'find')

    # выбор раздела аккардеона
    def get__accordion_chapter(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__accordion_chapter.format(name), 'accordion_chapter')

    # Выбор поля
    def get__input(self, name: str):
        return self.is_visible('xpath', self.__input.format(name), 'input')

    # открыть спиок категорий
    def get_cat_section(self) -> WebElement:
        return self.is_visible('xpath', self.__cat_section, 'cat_section')

    # выбрать категорию
    def get_cat(self) -> WebElement:
        return self.is_visible('xpath', self.__cat, 'cat')

    # модель по ПТС
    def get_type_vehicle_section(self) -> WebElement:
        return self.is_visible('xpath', self.__type_vehicle_section, 'type_vehicle_section')

    # модель по ПТС
    def get_vehicle_type(self) -> WebElement:
        return self.is_visible('xpath', self.__type_vehicle, 'type_vehicle')

    # выбор раздела аккардеона
    def get_accardion_chapter(self, name: str) -> WebElement:
        return self.is_visible('xpath', self.__accordion_chapter.format(name), 'vehicle_section')

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

    # кнопка сохранить
    def get_vehicle_save(self) -> WebElement:
        return self.is_visible('xpath', self.__vehicle_save, 'vehicle_save')

    # проверка о загрузке страницы проверкой доступности кнопки сохранить
    def get_wait_load_dom_Journal(self):
        if self.to_be_clickable('xpath', self.__button_add_vehicle, 'button_add_vehicle'):
            return True
        else:
            return False

    # проверка о загрузке страницы проверкой доступности кнопки сохранить
    def get_wait_load_dom_add(self):
        if self.to_be_clickable('xpath', self.__vehicle_save, 'vehicle_save'):
            return True
        else:
            return False

    # Получаем журнал ТС -> список webElement
    def get_vehicle_Journal(self) -> list[WebElement]:
        return self.are_visible('xpath', self.__vehicle_Journal, 'vehicle_Journal')

    # Получаем список WebElement ->  возвращаем строку елементов
    def get_vehicle_Journal_text(self) -> str:
        return Utils.join_strings(Utils.get_text_from_webelements(self.get_vehicle_Journal()))

    # кнопка Загрузить ТС из файла
    def get_button_vehicle_import(self) -> WebElement:
        return self.is_visible('xpath', self.__button_vehicle_import, 'button_vehicle_import')

    # область для загрузки файлов
    def get_uploader(self) -> WebElement:
        return self.is_visible('xpath', self.__uploader, 'upload')

    def get_close(self):
        return self.is_visible('xpath', self.__close, 'close')

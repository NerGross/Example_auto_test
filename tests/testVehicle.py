import allure
import pytest
import config
from time import sleep
from datetime import datetime
from pom.enter import Enter
from pom.vehicle import Vehicle
from random import choices
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures('setup')
class TestVehicle:

    def enter(self):
        enter = Enter(self.driver)
        with allure.step('Вход в ЛК'):
            enter.get_login().send_keys(config.login_admin)
            enter.get_password().send_keys(config.password_admin)
            enter.get_button_enter().click()
        with allure.step('Выбор организации'):
            enter.get_employee_list().click()
        with allure.step('Переход Объекты страхование - Транспортные средства'):
            enter.get_menu_item().click()
            enter.get_menu_item_child().click()

    @allure.story('Ручное добавление ТС')
    def test_manual(self):
        """
        Ручное добавление ТС
        """

        vehicle = Vehicle(self.driver)
        with allure.step('Вход в ЛК'):
            TestVehicle().enter()
        with allure.step('Загрузки страницы журнал ТС'):
            while not vehicle.get_wait_load_dom_Journal():
                sleep(1)
        with allure.step('Переход в добавление ТС'):
            vehicle.get_button_add_vehicle().click()
        with allure.step('Загрузки страницы добавления ТС'):
            while not vehicle.get_wait_load_dom_add():
                sleep(1)
        with allure.step('марка'):
            vehicle.get_mark().send_keys('robot')
        with allure.step('модель'):
            vehicle.get_model().send_keys('manual')
        with allure.step('категория'):
            vehicle.get_cat_section().click()
            sleep(1)
            vehicle.get_cat().click()
        with allure.step('тип'):
            vehicle.get_type_vehicle_section().click()
            sleep(1)
            vehicle.get_vehicle_type().click()
        with allure.step('Мощность'):
            vehicle.get_power().send_keys('250')
        with allure.step('год'):
            current_day = datetime.now()
            vehicle.get_year().send_keys(current_day.year)
        with allure.step('vin'):
            VIN = choices(config.str_vin, k=17)
            vehicle.get_vin().send_keys(VIN)
        with allure.step('Закрытие раздела ТС'):
            vehicle.get_vehicle_section().click()
        with allure.step('Открытие раздела докумаент на  ТС'):
            vehicle.get_doc_section().click()
        with allure.step('тип документа'):
            vehicle.get_doc_type_section().click()
            sleep(1)
            vehicle.get_doc_type().click()
        with allure.step('Серия документа о регистрации'):
            vehicle.get_doc_series().send_keys(choices(config.str_number, k=2) + choices(config.str_rus, k=2))
        with allure.step('Номер документа о регистрации'):
            vehicle.get_doc_number().send_keys(
                "00{:02}{:02}".format(current_day.day, current_day.month))
        with allure.step('Номер документа о регистрации'):
            vehicle.get_doc_date().send_keys(
                "{:02}.{:02}.{:04}".format(current_day.day, current_day.month, current_day.year))
        with allure.step('сохраняем'):
            vehicle.get_vehicle_save().click()
        with allure.step('Загрузки страницы журнал ТС'):
            while not vehicle.get_wait_load_dom_Journal():
                sleep(1)
        with allure.step('Обновление страницы'):
            vehicle.driver.refresh()
        with allure.step('Загрузки страницы журнал ТС'):
            while not vehicle.get_wait_load_dom_Journal():
                sleep(1)
        with allure.step('Проверка добавления ТС'):
            if "".join(VIN) in vehicle.get_vehicle_Journal_text():
                result = True
            else:
                result = False
            assert result == True

    @allure.story('Импорт ТС')
    def test_import(self):
        """
        Импорт ТС
        """
        vehicle = Vehicle(self.driver)
        with allure.step('Вход в ЛК'):
            TestVehicle().enter()
        with allure.step('Загрузки страницы журнал ТС'):
            while not vehicle.get_wait_load_dom_Journal():
                sleep(1)
        with allure.step('Переход в импорт'):
            vehicle.get_button_vehicle_import().click()
        sleep(1)
        with allure.step('загрузка файла'):
            vehicle.get_close().click()
           # vehicle.get_uploader().send_keys('C:\suburb.xlsx')
        sleep(10)

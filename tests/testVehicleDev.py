import allure
import pytest
import config
from time import sleep
from datetime import datetime
from pom.enter import Enter
from pom.vehicle import Vehicle
from random import choices, choice
from openpyxl import load_workbook

@pytest.mark.usefixtures('setup')
class TestVehicle:

    def enter(self):
        enter = Enter(self.driver)
        with allure.step('Вход в ЛК'):
            enter.get_login().send_keys(config.login_admin)
            enter.get_password().send_keys(config.password_admin)
            enter.get_button_enter().click()
        sleep(1)
        with allure.step('Выбор организации'):
            enter.get_employee_list().click()
        sleep(1)
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
            while not vehicle.get_wait_load_dom("Добавить ТС"):
                sleep(1)
        # Раздел "ТС"
        with allure.step("Переход в добавление ТС"):
            vehicle.get_button("Добавить ТС").click()
        with allure.step('Загрузки страницы добавления ТС'):
            while not vehicle.get_wait_load_dom("Сохранить"):
                sleep(1)
        with allure.step("Марка"):
            vehicle.get_drop_down("Марка").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Марка"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Марка"]).click()
        with allure.step("Модель"):
            vehicle.get_drop_down("Модель").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Модель"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Модель"]).click()
        with allure.step("Модификация"):
            vehicle.get_drop_down("Модификация").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Модификация"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Модификация"]).click()
        with allure.step("Марка по ПТС"):
            vehicle.get__input("Марка по ПТС").send_keys(config.vehicle_dict["Марка по ПТС"])
        with allure.step("Модель по ПТС"):
            vehicle.get__input("Модель по ПТС").send_keys(config.vehicle_dict["Модель по ПТС"])
        with allure.step("Категория"):
            vehicle.get_drop_down("Категория").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Категория"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Категория"]).click()
        with allure.step("Тип ТС"):
            vehicle.get_drop_down("Тип ТС").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Тип ТС"])
            vehicle.get_drop_down_meaning(config.vehicle_dict["Тип ТС"]).click()
        # with allure.step("Мощность, л.с. (для категории В)"):
        #    vehicle.get__input("Мощность, л.с. (для категории В)").send_keys(config.vehicle_dict["Мощность"])
        with allure.step("Год выпуска"):
            current_day = datetime.now()
            vehicle.get__input("Год выпуска").send_keys(current_day.year)
        with allure.step("Регистрационный номер"):
            vehicle.get__input("Регистрационный номер").send_keys(
                (choices(config.str_rus, k=1)) + (choices(config.str_number, k=3)) + (choices(config.str_rus, k=2))
                + (choices(config.str_number, k=3)))
        with allure.step("VIN"):
            VIN = choices(config.str_vin, k=17)
            vehicle.get__input("VIN").send_keys(VIN)
        with allure.step("Закрытие раздела ТС"):
            vehicle.get_accordion_chapter("Транспортное средство").click()
        # Раздел "документы на ТС"
        with allure.step("Открытие раздела докумаент на  ТС"):
            vehicle.get_accordion_chapter("Документ на ТС").click()
        with allure.step("Тип документа TC"):
            vehicle.get_drop_down("Тип документа TC").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Тип документа TC"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Тип документа TC"]).click()
        with allure.step('Серия документа о регистрации'):
            vehicle.get_doc_vehicle_series().send_keys(choices(config.str_number, k=2) + choices(config.str_rus, k=2))
        with allure.step('Номер документа о регистрации'):
            vehicle.get_doc_vehicle_number().send_keys(
                "00{:02}{:02}".format(current_day.day, current_day.month))
        with allure.step('Номер документа о регистрации'):
            vehicle.get_doc_vehicle_date().send_keys(
                "{:02}.{:02}.{:04}".format(current_day.day, current_day.month, current_day.year))
        with allure.step("Закрытие раздела докумаент на  ТС"):
            vehicle.get_accordion_chapter("Документ на ТС").click()
        # Раздел документы на ТО
        with allure.step("Открытие раздела документ на  ТО"):
            vehicle.get_accordion_chapter("Документ на ТО").click()
        with allure.step("Тип документа TO"):
            vehicle.get_drop_down("Тип документа TO").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Тип документа TO"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Тип документа TO"]).click()
        with allure.step("Номер документа TO"):
            vehicle.get__input("Номер документа TO").send_keys(choices(config.str_number, k=21))
        with allure.step("Дата выдачи документа TO"):
            vehicle.get_doc_TO_date().send_keys(
                "{:02}.{:02}.{:04}".format(current_day.day, current_day.month, current_day.year))
        # конец заполнения
        with allure.step('Cохраняем'):
            vehicle.get_button("Сохранить").click()
        with allure.step("Загрузки страницы журнал ТС"):
            while not vehicle.get_wait_load_dom("Добавить ТС"):
                sleep(1)
        with allure.step("Обновление страницы"):
            vehicle.driver.refresh()
        with allure.step("Загрузки страницы журнал ТС"):
            while not vehicle.get_wait_load_dom("Добавить ТС"):
                sleep(1)
        with allure.step("Проверка добавления ТС"):
            if "".join(VIN) in vehicle.get_vehicle_Journal():
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
        with allure.step("Вход в ЛК"):
            TestVehicle().enter()
        with allure.step("Ожиданеи загрузки страницы журнал ТС"):
            while not vehicle.get_wait_load_dom("Добавить ТС"):
                sleep(1)
        with allure.step("Переход в импорт"):
            vehicle.get_button("Загрузить ТС из файла").click()
        with allure.step("Формируем файл"):
            wb = load_workbook(config.url_file)
            sheet = wb.active
            current_day = datetime.now()
            sheet['B4'] = config.vehicle_dict["ИНН_Моэск"]
            sheet['C4'] = config.vehicle_dict["КПП_Моэск"]
            sheet['I4'] = "".join(choices(config.str_vin, k=17))
            sheet['L4'] = "".join((choices(config.str_rus, k=1)) + (choices(config.str_number, k=3)) +
                                  (choices(config.str_rus, k=2)) + (choices(config.str_number, k=3)))
            sheet['S4'] = ("00{:02}{:02}".format(current_day.day, current_day.month))
            wb.save(config.url_file)
            wb.close()
        sleep(1)
        with allure.step("Выбор шаблона"):
            sleep(1)
            if vehicle.get_template().text != "Шаблон ТС (стандартный)":
                vehicle.get_template().click()
                vehicle.get_drop_down_find().send_keys("Шаблон ТС (стандартный)")
                vehicle.get_drop_down_find().send_keys('\n')
                vehicle.get_drop_down_meaning("Шаблон ТС (стандартный)").click()
        sleep(1)
        with allure.step("загрузка файла"):
            vehicle.get_upload().send_keys(config.url_file)
        with allure.step('Ожидание загрузки файла'):
            while not vehicle.get_wait_load_dom("Загрузить"):
                sleep(1)
        with allure.step('Загрузить'):
            vehicle.get_button("Загрузить").click()
        with allure.step('Ожидание загрузки страницы'):
            while not vehicle.get_wait_load_dom("К списку ТС"):
                sleep(1)
        with allure.step("Проверка добавления ТС"):
            assert vehicle.get_upload_stat() == vehicle.UPLOAD_STAT

import allure
import pytest
import config
from datetime import datetime
from TestEnter.pom.enterLocator import EnterLocator
from TestVehicle.pom.vehicleLocator import VehicleLocator
from random import choices
from openpyxl import load_workbook


@pytest.mark.usefixtures('setup')
class TestVehicle:

    @allure.story('Ручное добавление ТС CС')
    def test_manual(self, login, vehicleFixture):
        """
        Ручное добавление ТС
        """
        login(self)
        vehicleFixture.vehicle_open_manual(self)
        vehicleFixture.vehicle(self)
        vehicleFixture.vehicle_doc_TC(self)
        vehicleFixture.vehicle_doc_TO(self)
        vehicleFixture.vehicle_close(self)

    @allure.story('Импорт ТС CС')
    def test_import(self):
        """
        Импорт ТС
        """
        vehicle = VehicleLocator(self.driver)
        with allure.step("Вход в ЛК"):
            TestVehicle().enter()
        with allure.step("Загрузки страницы ТС"):
            assert vehicle.get_button("Добавить ТС")
        with allure.step("Переход в импорт"):
            vehicle.get_button("Загрузить ТС из файла").click()
        with allure.step("Загрузки страницы импорта ТС"):
            # vehicle.get_not_button("Добавить ТС")
            assert vehicle.get_button("Закрыть")
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
        with allure.step("Выбор шаблона"):
            if vehicle.get_template().text != "Шаблон ТС (стандартный)":
                vehicle.get_template().click()
                vehicle.get_drop_down_find().send_keys("Шаблон ТС (стандартный)")
                vehicle.get_drop_down_find().send_keys('\n')
                vehicle.get_drop_down_meaning("Шаблон ТС (стандартный)").click()
        with allure.step("загрузка файла"):
            vehicle.get_upload().send_keys(config.url_file)
        with allure.step('Ожидание загрузки файла'):
            assert vehicle.get_button("Загрузить")
        # конец заполнения
        with allure.step('Загрузить'):
            vehicle.get_button("Загрузить").click()
        with allure.step("Загрузки промежуточной таблицы"):
            vehicle.get_not_button("Загрузить")
            assert vehicle.get_button("К списку ТС")
        with allure.step("Проверка добавления ТС"):
            assert vehicle.get_upload_stat() == vehicle.UPLOAD_STAT

import random

import allure
import config
from datetime import datetime
from TestVehicle.pom.vehicleLocator import VehicleLocator
from random import choices, choice


class VehicleManualFixture:
    __param = choices(config.str_vin, k=17)

    def __init__(self):
        self.driver = None

    def vehicle_open(self):
        """Открытие формы добавления ТС"""
        vehicle = VehicleLocator(self.driver)
        with allure.step("Загрузки страницы ТС"):
            assert vehicle.get_button("Добавить ТС")
        with allure.step("Переход в добавление ТС"):
            vehicle.get_button("Добавить ТС").click()
        with allure.step("Загрузки страницы добавления ТС"):
            vehicle.get_not_button("Добавить ТС")
            assert vehicle.get_button("Сохранить")

    def vehicle(self):
        """Раздел "ТС"""
        vehicle = VehicleLocator(self.driver)
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
        with allure.step("Год выпуска"):
            current_day = datetime.now()
            vehicle.get__input("Год выпуска").send_keys(current_day.year)
        # key_parameter = choice["Регистрационный номер", "№ шасси", "№ кузова", "VIN"]
        # if key_parameter == "Регистрационный номер":
        with allure.step("Регистрационный номер"):
            vehicle.get__input("Регистрационный номер").send_keys(
                (choices(config.str_rus, k=1)) + (choices(config.str_number, k=3)) + (choices(config.str_rus, k=2))
                + (choices(config.str_number, k=3)))
        # else:
        #    with allure.step(key_parameter):
        #        vehicle.get__input(key_parameter).send_keys(VehicleManualFixture.__param)
        with allure.step("Закрытие раздела ТС"):
            vehicle.get_accordion_chapter("Транспортное средство").click()

    def vehicle_owner(self):
        """Раздел "Страхователь"""
        vehicle = VehicleLocator(self.driver)
        with allure.step("Отрытие раздела Страхователь"):
            vehicle.get_accordion_chapter("Страхователь").click()
        with allure.step("Компания-страхователь"):
            vehicle.get_drop_down("Компания-страхователь").click()
            vehicle.get_drop_down_meaning(config.vehicle_dict["Компания"]).click()
        with allure.step("Закрытие раздела Страхователь"):
            vehicle.get_accordion_chapter("Страхователь").click()

    def vehicle_doc(self):
        """Раздел "Документа на ТС"""
        vehicle = VehicleLocator(self.driver)
        current_day = datetime.now()
        with allure.step("Открытие раздела документ на  ТС"):
            vehicle.get_accordion_chapter("Документ на ТС").click()
        with allure.step("Тип документа TC"):
            vehicle.get_drop_down("Тип документа TC").click()
            vehicle.get_drop_down_find().send_keys(config.vehicle_dict["Тип документа TC"])
            vehicle.get_drop_down_find().send_keys('\n')
            vehicle.get_drop_down_meaning(config.vehicle_dict["Тип документа TC"]).click()
        with allure.step('Серия документа о регистрации'):
            vehicle.get_doc_vehicle_series().send_keys(choices(config.str_number, k=2) + choices(config.str_rus, k=2))
        with allure.step('Номер документа о регистрации'):
            vehicle.get_doc_vehicle_number().send_keys(choices(config.str_number, k=6))
        with allure.step('Номер документа о регистрации'):
            vehicle.get_doc_vehicle_date().send_keys(
                "{:02}.{:02}.{:04}".format(current_day.day, current_day.month, current_day.year))
        with allure.step("Закрытие раздела документ на  ТС"):
            vehicle.get_accordion_chapter("Документ на ТС").click()

    def vehicle_doc_to(self):
        """Раздел "Документа ны ТО"""
        vehicle = VehicleLocator(self.driver)
        current_day = datetime.now()
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
            vehicle.get_doc_to_date().send_keys(
                "{:02}.{:02}.{:04}".format(current_day.day, current_day.month, current_day.year))

    def vehicle_close(self):
        """Закрытие формы добавления ТС"""
        vehicle = VehicleLocator(self.driver)
        with allure.step('Сохранить'):
            vehicle.get_button("Сохранить").click()
        with allure.step("Загрузки страницы журнал ТС"):
            vehicle.get_not_button("Сохранить")
            assert vehicle.get_button("Добавить ТС")
        with allure.step("Проверка добавления ТС"):
            if "".join(VehicleManualFixture.__param) in vehicle.get_vehicle_journal():
                result = True
            else:
                result = False
            assert result == True

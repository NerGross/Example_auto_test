import allure
import pytest
import config
from datetime import datetime
from pom.enter import Enter
from pom.vehicle import Vehicle
from random import choices
from openpyxl import load_workbook


@pytest.mark.usefixtures('setup')
class TestVehicle:

    def enter(self):
        enter = Enter(self.driver)
        with allure.step("Загрузки страницы ввода логина и пароля"):
            enter.get_button("Войти")
        with allure.step('Вход в ЛК'):
            enter.get_auth("Логин").send_keys(config.login_admin)
            enter.get_auth("Пароль").send_keys(config.password_admin)
            enter.get_button("Войти").click()
        with allure.step("Загрузки страницы выбор компании"):
            enter.get_not_button("Войти")
            assert enter.get_company("МОЭСК")
        with allure.step('Выбор организации'):
            enter.get_company("МОЭСК").click()
        with allure.step("Загрузки страницы Договоры"):
            enter.get_not_company("Моэкс")
            assert enter.get_drop_down_meaning("Страхование ТС")
        with allure.step('Переход по меню'):
            enter.get_menu("Объекты страхования").click()
            enter.get_menu("Транспортные средства").click()
        with allure.step("Транспортные средства"):
            enter.get_not_drop_down_meaning("Страхование ТС")

    @allure.story('Ручное добавление ТС CС')
    def test_manual(self):
        """
        Ручное добавление ТС
        """

        vehicle = Vehicle(self.driver)
        with allure.step("Вход в ЛК"):
            TestVehicle().enter()
        with allure.step("Загрузки страницы ТС"):
            assert vehicle.get_button("Добавить ТС")
        with allure.step("Переход в добавление ТС"):
            vehicle.get_button("Добавить ТС").click()
        with allure.step("Загрузки страницы добавления ТС"):
            vehicle.get_not_button("Добавить ТС")
            assert vehicle.get_button("Сохранить")
        # Раздел "ТС"
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
            vehicle.get_not_button("Сохранить")
            assert vehicle.get_button("Добавить ТС")
        with allure.step("Проверка добавления ТС"):
            if "".join(VIN) in vehicle.get_vehicle_Journal():
                result = True
            else:
                result = False
            assert result == True

    @allure.story('Импорт ТС CС')
    def test_import(self):
        """
        Импорт ТС
        """
        vehicle = Vehicle(self.driver)
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
            assert vehicle.get_button("Загрузить1")
        # конец заполнения
        with allure.step('Загрузить'):
            vehicle.get_button("Загрузить").click()
        with allure.step("Загрузки промежуточной таблицы"):
            vehicle.get_not_button("Загрузить")
            assert vehicle.get_button("К списку ТС")
        with allure.step("Проверка добавления ТС"):
            assert vehicle.get_upload_stat() == vehicle.UPLOAD_STAT

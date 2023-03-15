import allure
import pytest
from time import sleep


@pytest.mark.usefixtures('setup')
class TestVehicle:

    @allure.story('Ручное добавление ТС c заполнением всех полей для CС')
    def test_manual_full(self, enter_fixture, vehicle_manual_fixture):
        """
        Ручное добавление ТС C заполнением всех полей для CC
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_manual_fixture.vehicle_open(self)
        vehicle_manual_fixture.vehicle(self)
        vehicle_manual_fixture.vehicle_doc(self)
        vehicle_manual_fixture.vehicle_doc_to(self)
        vehicle_manual_fixture.vehicle_close(self)

    @allure.story('Ручное добавление ТС c заполнением обязательных полей для СC')
    def test_manual(self, enter_fixture, vehicle_manual_fixture):
        """
        Ручное добавление ТС с заполнением обязательных полей для CC
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_manual_fixture.vehicle_open(self)
        vehicle_manual_fixture.vehicle(self)
        vehicle_manual_fixture.vehicle_doc(self)
        vehicle_manual_fixture.vehicle_close(self)

    @allure.story('Импорт ТС CС')
    def test_import(self, enter_fixture, vehicle_import_fixture):
        """
        Импорт ТС для CC
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_import_fixture.vehicle_open(self)
        vehicle_import_fixture.vehicle_file(self)
        vehicle_import_fixture.vehicle_import(self)
        vehicle_import_fixture.vehicle_close(self)

    @allure.story('Импорт ТС CС')
    def test_import_addition(self, enter_fixture, vehicle_import_fixture):
        """
        Импорт ТС для CC (проверка автодополнения)
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_import_fixture.vehicle_open(self)
        vehicle_import_fixture.vehicle_file_addition(self)
        vehicle_import_fixture.vehicle_import(self)
        vehicle_import_fixture.vehicle_close(self)

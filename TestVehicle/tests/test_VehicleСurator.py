import allure
import pytest


@pytest.mark.usefixtures('setup')
class TestVehicle:

    @allure.story('Ручное добавление ТС c заполнением всех полей для CК')
    def test_manual(self, enter_fixture, vehicle_manual_fixture):
        """
        Ручное добавление ТС с заполнением всех полей для СК
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_manual_fixture.vehicle_open(self)
        vehicle_manual_fixture.vehicle(self)
        vehicle_manual_fixture.vehicle_owner(self)
        vehicle_manual_fixture.vehicle_doc(self)
        vehicle_manual_fixture.vehicle_doc_to(self)
        vehicle_manual_fixture.vehicle_close(self)

    @allure.story('Ручное добавление ТС c заполнением обязательных полей для СК')
    def test_manual(self, enter_fixture, vehicle_manual_fixture):
        """
        Ручное добавление ТС с заполнением обязательных полей для СК
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_manual_fixture.vehicle_open(self)
        vehicle_manual_fixture.vehicle(self)
        vehicle_manual_fixture.vehicle_owner(self)
        vehicle_manual_fixture.vehicle_doc(self)
        vehicle_manual_fixture.vehicle_close(self)

    @allure.story('Импорт ТС CК')
    def test_import(self, enter_fixture, vehicle_import_fixture):
        """
        Импорт ТС для СК
        """
        enter_fixture.enter_sk(self)
        enter_fixture.transition_to_vehicle(self)
        vehicle_import_fixture.vehicle_open(self)
        vehicle_import_fixture.vehicle_owner(self)
        vehicle_import_fixture.vehicle_file(self)
        vehicle_import_fixture.vehicle_import(self)
        vehicle_import_fixture.vehicle_close(self)

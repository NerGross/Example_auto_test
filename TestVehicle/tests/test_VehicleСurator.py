import allure
import pytest


@pytest.mark.usefixtures('setup')
class TestVehicle:

    @allure.story('Ручное добавление ТС c заполнением всех полей для CК')
    def test_manual(self, enterFixture, vehicleManualFixture):
        """
        Ручное добавление ТС c заполнением всех полей для CК
        """
        enterFixture.enter_SK(self)
        enterFixture.transition_to_vehicle(self)
        vehicleManualFixture.vehicle_open(self)
        vehicleManualFixture.vehicle(self)
        vehicleManualFixture.vehicle_owner(self)
        vehicleManualFixture.vehicle_doc_TC(self)
        vehicleManualFixture.vehicle_doc_TO(self)
        vehicleManualFixture.vehicle_close(self)

    @allure.story('Ручное добавление ТС c заполнением обязательных полей для СК')
    def test_manual(self, enterFixture, vehicleManualFixture):
        """
        Ручное добавление ТС c заполнением обязательных полей для СК
        """
        enterFixture.enter_SK(self)
        enterFixture.transition_to_vehicle(self)
        vehicleManualFixture.vehicle_open(self)
        vehicleManualFixture.vehicle(self)
        vehicleManualFixture.vehicle_owner(self)
        vehicleManualFixture.vehicle_doc_TC(self)
        vehicleManualFixture.vehicle_close(self)

    @allure.story('Импорт ТС CК')
    def test_import(self, enterFixture, vehicleImportFixture):
        """
        Импорт ТС для СК
        """
        enterFixture.enter_SK(self)
        enterFixture.transition_to_vehicle(self)
        vehicleImportFixture.vehicle_open(self)
        vehicleImportFixture.vehicle_owner(self)
        vehicleImportFixture.vehicle_file(self)
        vehicleImportFixture.vehicle_import(self)
        vehicleImportFixture.vehicle_close(self)

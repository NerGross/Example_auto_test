import allure
import pytest


@pytest.mark.usefixtures('setup')
class TestVehicle:

    @allure.story('Ручное добавление ТС c заполнением всех полей для CС')
    def test_manual(self, enterFixture, vehicleManualFixture):
        """
        Ручное добавление ТС c заполнением всех полей для CС
        """
        enterFixture.enter_SS(self)
        enterFixture.transition_to_vehicle(self)
        vehicleManualFixture.vehicle(self)
        vehicleManualFixture.vehicle_doc_TC(self)
        vehicleManualFixture.vehicle_doc_TO(self)
        vehicleManualFixture.vehicle_close(self)

    @allure.story('Ручное добавление ТС c заполнением обязательных полей для СC')
    def test_manual(self, enterFixture, vehicleManualFixture):
        """
        Ручное добавление ТС c заполнением обязательных полей для СC
        """
        enterFixture.enter_SS(self)
        enterFixture.transition_to_vehicle(self)
        vehicleManualFixture.vehicle_open(self)
        vehicleManualFixture.vehicle(self)
        vehicleManualFixture.vehicle_doc_TC(self)
        vehicleManualFixture.vehicle_close(self)

    @allure.story('Импорт ТС CС')
    def test_import(self, enterFixture, vehicleImportFixture):
        """
        Импорт ТС для СC
        """
        enterFixture.enter(self)
        enterFixture.transition_to_vehicle(self)
        vehicleImportFixture.vehicle_open(self)
        vehicleImportFixture.vehicle_file(self)
        vehicleImportFixture.vehicle_import(self)
        vehicleImportFixture.vehicle_close(self)

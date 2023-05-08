import pytest
from TestVehicle.pages.vehicleImportFixture import VehicleImportFixture
from TestVehicle.pages.vehicleManualFixture import VehicleManualFixture


@pytest.fixture(scope="function")
def vehicle_manual_fixture():
    return VehicleManualFixture


@pytest.fixture(scope="function")
def vehicle_import_fixture():
    return VehicleImportFixture



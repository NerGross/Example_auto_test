import pytest
from TestVehicle.pom.vehicleImportFixture import VehicleImportFixture
from TestVehicle.pom.vehicleManualFixture import VehicleManualFixture


@pytest.fixture(scope="function")
def vehicle_manual_fixture():
    return VehicleManualFixture


@pytest.fixture(scope="function")
def vehicle_import_fixture():
    return VehicleImportFixture

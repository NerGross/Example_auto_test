import pytest
from TestVehicle.pom.VehicleImportFixture import VehicleImportFixture
from TestVehicle.pom.VehicleManualFixture import VehicleManualFixture


@pytest.fixture(scope="function")
def vehicleManualFixture():
    return VehicleManualFixture


@pytest.fixture(scope="function")
def vehicleImportFixture():
    return VehicleImportFixture

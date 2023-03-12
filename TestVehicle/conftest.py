import pytest
from TestVehicle.pom.vehicleFixture import VehicleFixture


@pytest.fixture(scope="function")
def vehicleFixture():
    return VehicleFixture

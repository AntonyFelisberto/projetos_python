import pytest
from car import Car

class TestCat(object):

    @pytest.fixture(scope="module")
    def my_cars(self):
        return Car(0,"off")

    def better_code(self,my_cars): #you can pass my_cars for another methods too
        my_cars.start()
        assert my_cars.state == "running"

    def test_start(self):
        my_car = Car(0,"off")
        my_car.start()

    def test_turn_off(self):
        my_car = Car(0,"running")
        my_car.turn_off()
        assert my_car.state == "off"

    def test_acceleration(self):
        my_car = Car(0,"off")
        my_car.accelerate()
        assert my_car.speed == 10

    def test_stop(self,my_cars):
        my_cars.stop()
        assert my_cars.speed == 0    
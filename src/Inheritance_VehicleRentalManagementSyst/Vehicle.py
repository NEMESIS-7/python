class Vehicle:
    _vehicle_id = ""
    _brand = ""
    _model = ""
    _is_available = True

    def __init__(self, _vehicle_id, _brand, _model):
        self._vehicle_id = _vehicle_id
        self._brand = _brand
        self._model = _model
        self._is_available = True

    def rent_vehicle(self):
        if self._is_available:
            self._is_available = False
            print(f"{self._brand} {self._model} has been rented successfully.")
        else:
            raise Exception("The vehicle is not available")

    def return_vehicle(self):
        if self._is_available:
            raise Exception("The vehicle is already returned/available")
        else:
            self._is_available = True
            print(f"{self._brand} {self._model} returned and is available")
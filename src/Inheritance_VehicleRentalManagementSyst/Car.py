from Vehicle import Vehicle


class Car(Vehicle):
    _seating_capacity = 0
    def __init__(self, _vehicle_id, _brand, _model, _seating_capacity):
        Vehicle.__init__(self, _vehicle_id, _brand, _model)
        self._seating_capacity = _seating_capacity

    def calculate_rental_cost(self, days):
        price = 1000 * days + self._seating_capacity * 50
        return f"Rental cost for {days} days is ${price}"


#Creating a car
car = Car(
    "02441156",
    "Ford",
    "Mustang Dark Horse",
    4
)

#Renting the car
try:
    car.rent_vehicle()
except Exception as e:
    print(str(e))

#Returning a car
try:
    car.return_vehicle()
except Exception as e:
    print(str(e))

#Calculating rental costs
print(car.calculate_rental_cost(5))
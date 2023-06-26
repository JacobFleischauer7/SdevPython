class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def main():
    vehicle_type = "car"  # Set the vehicle type to "car" for this example

    print("Enter the details for the car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nVehicle details:")
    print("Vehicle type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)


if __name__ == "__main__":
    main()
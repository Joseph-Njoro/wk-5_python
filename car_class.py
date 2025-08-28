class Vehicle:
    """Base class for all vehicles (inheritance layer)"""
    
    def __init__(self, make, model, year, color, price):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._price = price
        self._mileage = 0
        self._is_running = False
    
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            print(f"{self._make} {self._model} engine started!")
        else:
            print("Engine is already running!")
    
    def stop_engine(self):
        if self._is_running:
            self._is_running = False
            print("Engine stopped.")
        else:
            print("Engine is already off!")
    
    def display_info(self):
        return f"{self._year} {self._make} {self._model} - Color: {self._color}, Price: ${self._price:,}, Mileage: {self._mileage} miles"
    
    # Getter methods (encapsulation)
    def get_make(self):
        return self._make
    
    def get_model(self):
        return self._model
    
    def get_year(self):
        return self._year
    
    def get_price(self):
        return self._price
    
    def get_mileage(self):
        return self._mileage


class Car(Vehicle):  # Inheritance
    """Car class inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, price, doors=4):
        super().__init__(make, model, year, color, price)  # Initialize parent class
        self._doors = doors  # New attribute specific to Car
    
    def drive(self, distance):
        if self._is_running:
            self._mileage += distance
            print(f"Driven {distance} miles. Total mileage: {self._mileage}")
        else:
            print("Start the engine first!")
    
    def honk(self):
        print("Beep! Beep!")
    
    def set_color(self, new_color):
        self._color = new_color
        print(f"Car color changed to {new_color}")
    
    # Method overriding (polymorphism)
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Doors: {self._doors}"


if __name__ == "__main__":
    print("VEHICLE INHERITANCE DEMONSTRATION\n")
    
    # Create different car objects
    cars = [
        Car("Toyota", "Camry", 2022, "Blue", 25000, 4),
        Car("Tesla", "Model 3", 2023, "White", 45000, 4)
    ]
    
    # Demonstrate the Car methods
    for i, car in enumerate(cars, 1):
        print(f"Car #{i}: {car.get_make()} {car.get_model()}")
        car.start_engine()
        car.drive(50)
        car.honk()
        
        # display_info() shows the overridden version with doors information
        print(car.display_info())
        print()

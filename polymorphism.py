class Vehicle:
    def move(self):
        print("This vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚢")

# Example usage
def demo_movements():
    vehicles = [Car(), Plane(), Boat()]

    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    demo_movements()
# Define the Engine class
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
        self.is_running = False  # Initial state of the engine

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.type_of_engine} engine is now running.")
        else:
            print(f"{self.type_of_engine} engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.type_of_engine} engine has stopped.")
        else:
            print(f"{self.type_of_engine} engine is already stopped.")

# Define the Car class
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start_car(self):
        print(f"Starting the {self.make} {self.model}...")
        self.engine.start()

    def stop_car(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()

# Creating an Engine instance
car_engine = Engine("V8")

# Creating a Car instance with the Engine instance
my_car = Car("Ford", "Mustang", car_engine)

# Using the Car methods, which internally control the Engine
my_car.start_car()
my_car.stop_car()

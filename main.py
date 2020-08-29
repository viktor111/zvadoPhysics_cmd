import math

# --- Equations ---


class Energy_Mass:
    def __init__(self):
        self.speed_of_light = 299792458.0
        self.info = "Calculate the stationary energy of an object by its mass"
        self.args = "1- mass"
        self.name = "Energy Mass Einstein"

    @staticmethod
    def calculate(self, mass):
        speed_of_light_squared = math.sqrt(self.speed_of_light)
        energy = mass * speed_of_light_squared
        return energy


class Newton_First_Law:
    def __init__(self):
        self.info = "Calculate newtons first law the force of an object by the mass and acceleration"
        self.args = "1- mass, 2- acceleration"
        self.name = "Newton first law"

    @staticmethod
    def calculate(mass, acceleration):
        force = mass * acceleration
        return force


class Speed_Distance:
    def __init__(self):
        self.info = "Calculate the speed per hour based on distance"
        self.args = "1- distance, 2- acceleration"
        self.name = "Speed Distnace"

    @staticmethod
    def calculate(distnace, time):
        result = distnace * time
        return result


class Acceleration:
    def __init__(self, final_velocity, initial_velocity, time_taken):
        self.final_velocity = final_velocity
        self.initial_velocity = initial_velocity
        self.time_taken = time_taken
        self.info = "Calculate the acceleration"
        self.args = "1- final_velocity, 2- initial_velocity, 3- time_taken"
        self.name = "Acceleration"

    @staticmethod
    def calculate(final_velocity, initial_velocity, time_taken):
        changing_velocity = final_velocity / initial_velocity
        result = changing_velocity / time_taken
        return result


class Density:
    def __init__(self):
        self.info = "Calculate the density of a body"
        self.args = "1- mass of the body, 2- volume of the body"
        self.name = "Density"

    @staticmethod
    def calculate(mass, volume):
        result = mass / volume
        return result


# --- Methods ---

def display_options():
    d = Density().name

while True:
    command = input()
    if "option" in command:
        display_options()

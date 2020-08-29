import math
from scipy import constants


# --- Equations ---

class Energy_Mass:
    def __init__(self, mass, info, args):
        self.mass = mass
        self.speed_of_light = 299792458.0
        self.info = "Calculate the stationary energy of an object by its mass"
        self.args = "1- mass"

    def calculate(self):
        speed_of_light_squared = math.sqrt(self.speed_of_light)
        energy = self.mass * speed_of_light_squared
        return energy


class Newton_First_Law:
    def __init__(self, mass, acceleration, info, args):
        self.mass = mass
        self.acceleration = acceleration
        self.info = "Calculate newtons first law the force of an object by the mass and acceleration"
        self.args = "1- mass, 2- acceleration"

    def calculate(self):
        force = self.mass * self.acceleration
        return force


class Speed_Distance:
    def __init__(self, distnace, time):
        self.distnace = distnace
        self.time = time
        self.info = "Calculate the speed per hour based on distance"
        self.args = "1- distance, 2- acceleration"

    def calculate(self):
        result = self.distnace * self.time
        return result


class Acceleration:
    def __init__(self, final_velocity, initial_velocity, time_taken):
        self.final_velocity = final_velocity
        self.initial_velocity = initial_velocity
        self.time_taken = time_taken
        self.info = "Calculate the acceleration"
        self.args = "1- final_velocity, 2- initial_velocity, 3- time_taken"

    def calculate(self):
        changing_velocity = self.final_velocity / self.initial_velocity
        result = changing_velocity / self.time_taken
        return result



# --- Methods ---

def display_options():
    print("1. Einstein mass-energy")
    print("2. Newtons First Law")


while True:
    command = input()
    if "option" in command:
        display_options()

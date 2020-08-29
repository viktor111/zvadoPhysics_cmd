import math


# --- Equations ---


class Energy_Mass:
    def __init__(self):
        self.id = 1
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
        self.id = 2
        self.info = "Calculate newtons first law the force of an object by the mass and acceleration"
        self.args = "1- mass, 2- acceleration"
        self.name = "Newton first law"

    @staticmethod
    def calculate(mass, acceleration):
        force = mass * acceleration
        return force


class Speed_Distance:
    def __init__(self):
        self.id = 3
        self.info = "Calculate the speed per hour based on distance"
        self.args = "1- distance, 2- acceleration"
        self.name = "Speed Distnace"

    @staticmethod
    def calculate(distnace, time):
        result = distnace * time
        return result


class Acceleration:
    def __init__(self):
        self.id = 4
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
        self.id = 5
        self.info = "Calculate the density of a body"
        self.args = "1- mass of the body, 2- volume of the body"
        self.name = "Density"

    @staticmethod
    def calculate(mass, volume):
        result = mass / volume
        return result


# --- Methods ---

def display_option_names():
    print("1. " + Energy_Mass().name)
    print("2. " + Newton_First_Law().name)
    print("3. " + Speed_Distance().name)
    print("4. " + Acceleration().name)
    print("5. " + Density().name)


def display_help():
    print("show - show all equation")
    print("info [number] - show the information about certain equation")
    print("arg [number] - show the arguments an equation accepts")
    print("bye - exit the program")


def display_info(argument):
    infos = [Energy_Mass().info, Newton_First_Law().info, Speed_Distance().info, Acceleration().info, Density().info]
    print(infos[argument])


def display_arguments(argument):
    args = [Energy_Mass().args, Newton_First_Law().args, Speed_Distance().args, Acceleration().args, Density().args]
    print(args[argument])


def read_command():
    command = input(">> ")
    if "show" in command:
        display_option_names()
    if "bye" in command:
        exit()
    if "help" in command:
        display_help()
    if "info" in command:
        try:
            args = command.split()
            number = int(args[1])
            display_info(number)
        except (IndexError, ValueError):
            print("Error in input try again")
            read_command()
    if "arg" in command:
        try:
            args = command.split()
            number = int(args[1])
            display_arguments(number)
        except (IndexError, ValueError):
            print("Error in input try again")
            read_command()


while True:
    try:
        read_command()
    except KeyboardInterrupt:
        print("Have a nice day :)")
        exit()

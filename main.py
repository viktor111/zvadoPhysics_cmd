import math

#--- Equations ---

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
	def __init__(self, mass, acceleration, info, args)
		self.mass = mass
		self.acceleration = acceleration
		self.info = "Calculate newtons first law the force of an object by the mass and acceleration"
		self.args = "1- mass, 2- acceleration"

	def calculate(self):
		force = self.mass * self.acceleration
		return force



#--- Methods ---

def display_options():
	print("1. Einstein mass-energy")
	print("2. Newtons First Law")

while True:
	
	

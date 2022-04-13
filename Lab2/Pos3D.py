from math import sqrt
from random import randint

class Pos3D:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

	def distanceTo(self, b):
		dx = self.x - b.x
		dy = self.y - b.y
		dz = self.z - b.z
		return sqrt(dx * dx + dy * dy + dz * dz)

	def setRandom(self):
		self.x = float(randint(-50, 50))
		self.y = float(randint(-50, 50))
		self.z = float(randint(-50, 50))

	def getPos(self):
		return str(self.x) + " " + str(self.y) + " " + str(self.z)
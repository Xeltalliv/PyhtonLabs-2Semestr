from math import sqrt
from random import randint
from Pos3D import Pos3D

class Cone:
	def __init__(self):
		self.base = Pos3D()
		self.top = Pos3D()
		self.radius = 0

	def setRandom(self):
		self.base.setRandom()
		self.top.setRandom()
		self.radius = float(randint(1, 5))

	def calcTvirna(self):
		return sqrt(self.base.distanceTo(self.top))

	def showInfo(self, i):
		print(" Конус №" + str(i) + ":")
		print("  Радіус основи: " + str(self.radius))
		print("  Центр основи: " + self.base.getPos())
		print("  Вершина: " + self.top.getPos())
		print("  Твірна: " + str(self.calcTvirna()) +"\n")

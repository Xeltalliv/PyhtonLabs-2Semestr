from math import sqrt
from TVector import TVector
from Config import EPSILON

class Vector3(TVector):
	def __init__(self, n=None):
		if n == None:
			self.x = self.y = self.z = 0
		else:
			print("Введіть 3D вектор №" + str(n) + ":")
			self.x = float(input(" X: "))
			self.y = float(input(" Y: "))
			self.z = float(input(" Z: "))
			print("\n")
	
	def getLength(self):
		return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
	
	def isParalellTo(self, other):
		return abs(self.normalizeAndDot(other) - 1) < EPSILON
	
	def isPerpendicularTo(self, other):
		return abs(self.normalizeAndDot(other)) < EPSILON
	
	def normalizeAndDot(self, other):
		len1 = self.getLength()
		if len1 == 0:
			len1 = 1
		x1n = self.x / len1
		y1n = self.y / len1
		z1n = self.z / len1

		len2 = other.getLength()
		if len2 == 0:
			len2 = 1
		x2n = other.getElem(0) / len2
		y2n = other.getElem(1) / len2
		z2n = other.getElem(2) / len2
	
		return x1n * x2n + y1n * y2n + z1n * z2n
	
	def getElem(self, n):
		if n == 0:
			return self.x
		if n == 1:
			return self.y
		if n == 2:
			return self.z
		return 0
	
	def __iadd__(self, other):
		self.x += other.getElem(0)
		self.y += other.getElem(1)
		self.z += other.getElem(2)
		return self
	
	def __str__(self):
		return str(self.x) + " " + str(self.y) + " " + str(self.z)
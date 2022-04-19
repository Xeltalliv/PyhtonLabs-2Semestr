#!/usr/bin/env python

class Numeral_16:
	def __init__(self, newValue):
		if isinstance(newValue, str):
			self.value = 0
			lowered = newValue.lower()
			allChars = "0123456789abcdef"
			for c in lowered:
				self.value = self.value * 16 + allChars.index(c)
		else:
			self.value = int(newValue)
	
	def __add__(self, other):
		if isinstance(other, Numeral_16):
			return Numeral_16(self.value + other.value)
		else:
			return Numeral_16(self.value + other)
	
	def __iadd__(self, other):
		if isinstance(other, Numeral_16):
			self.value += other.value
		else:
			self.value += other
		return self
	
	def toInt(self):
		return self.value
	
	def toString(self):
		allChars = "0123456789ABCDEF"
		tempValue = self.value
		outp = ""
		for i in range(8):
			outp = allChars[tempValue % 16] + outp
			tempValue //= 16
		return outp

	def __str__(self):
		return "0x"+self.toString()
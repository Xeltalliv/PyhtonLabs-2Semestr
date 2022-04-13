#!/usr/bin/env python

from Cone import Cone
from ConeOperations import randomizeCones, displayCones, findMax

coneCount = 20

def main():
	print("ЛАБОРАТОРНА РОБОТА 2:\n")
	cones = [Cone() for x in range(coneCount)]
	randomizeCones(cones)
	displayCones(cones)

	maxIndex = findMax(cones)
	print("Найбільшу твірну має конус №" + str(maxIndex))

main()
	
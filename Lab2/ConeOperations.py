def randomizeCones(cones):
	for i in range(len(cones)):
		cones[i].setRandom()

def displayCones(cones):
	print("Конуси:")
	for i in range(len(cones)):
		cones[i].showInfo(i)

def findMax(cones):
	maxVal = 0
	maxIndex = -1
	for i in range(len(cones)):
		val = cones[i].calcTvirna()
		if val > maxVal:
			maxVal = val
			maxIndex = i

	return maxIndex
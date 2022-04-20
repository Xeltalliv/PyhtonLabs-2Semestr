class TNode:
	def __init__(self):
		self.value = 0
		left = None
		right = None

	def insertToTree(self, insert):
		if insert.value > self.value:
			if self.right == None:
				self.right = insert
			else:
				self.right.insertToTree(insert)
		elif insert.value < self.value:
			if self.left == None:
				self.left = insert
			else:
				self.left.insertToTree(insert)
	
	def findMax(self):
		if self.right == None:
			return self.value
		else:
			return self.right.findMax()
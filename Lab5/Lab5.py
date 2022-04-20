#!/usr/bin/env python

from TNode import TNode

def main():
	print("ЛАБОРАТОРНА РОБОТА 5\n")
	print("Бінарні дерева")

	rootNode = None
	nodeCount = int(input("Кількість елементів в дереві: "))
	for i in range(nodeCount):
		node = TNode()
		node.value = float(input(" Елемент " + str(i+1) + ": "))
		node.left = node.right = None
		if rootNode == None:
			rootNode = node
		else:
			rootNode.insertToTree(node)

	if rootNode != None:
		print("\nМаксимальне значення: " + str(rootNode.findMax()))

main()

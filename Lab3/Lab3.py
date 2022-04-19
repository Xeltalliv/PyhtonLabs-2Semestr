#!/usr/bin/env python

from Numeral_16 import Numeral_16

def main():
	N1 = Numeral_16(12)
	N2 = Numeral_16("1f")
	N3 = Numeral_16("A0")
	print("Задаємо початкові значення на 12, \"1f\" та \"A0\"")
	print("N1: "+str(N1))
	print("N2: "+str(N2))
	print("N3: "+str(N3))

	print("\nПісля N1+=1")
	N1 += 1
	print("N1: "+str(N1))

	print("\nПісля N2+=4")
	N2 += 4
	print("N2: "+str(N2))

	print("\nПісля N3 = N1 + N2")
	N3 = N1 + N2
	print("N3: "+str(N3))

main()
#!/usr/bin/env python

from Vector2 import Vector2
from Vector3 import Vector3

def main():
	print("ЛАБОРАТОРНА РОБОТА 4\n")

	vec2A = Vector2(1)
	vec2B = Vector2(2)
	vec2C = Vector2(3)

	vec3A = Vector3(1)
	vec3B = Vector3(2)
	vec3C = Vector3(3)
	vec3D = Vector3(4)

	sum1 = 0
	if vec2B.isParalellTo(vec2A): sum1 += vec2B.getLength()
	if vec2C.isParalellTo(vec2A): sum1 += vec2C.getLength()
	if vec3A.isParalellTo(vec2A): sum1 += vec3A.getLength()
	if vec3B.isParalellTo(vec2A): sum1 += vec3B.getLength()
	if vec3C.isParalellTo(vec2A): sum1 += vec3C.getLength()
	if vec3D.isParalellTo(vec2A): sum1 += vec3D.getLength()

	print("Сумма довжин векторів що паралельні першому 2Д вектору: " + str(sum1))

	sum2 = Vector3()
	if vec2A.isPerpendicularTo(vec3A): sum2 += vec2A
	if vec2B.isPerpendicularTo(vec3A): sum2 += vec2B
	if vec2C.isPerpendicularTo(vec3A): sum2 += vec2C
	if vec3B.isPerpendicularTo(vec3A): sum2 += vec3B
	if vec3C.isPerpendicularTo(vec3A): sum2 += vec3C
	if vec3D.isPerpendicularTo(vec3A): sum2 += vec3D
	
	print("Сумма векторів що перпендикулярні першому 3Д вектору: " + str(sum2))

main()

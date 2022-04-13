#!/usr/bin/env python

def main():
	mstr = enterFromKeyboard();

	print("Вихідний файл:\n"+mstr+"\n\n\n");

	fileA, fileB = fillOtherFiles(mstr)

	print("Необроблений непарний файл:\n" + myJoin(fileA, "\n") + "\n\n\n")
	print("Необроблений парний файл:\n" + myJoin(fileB, "\n") + "\n\n\n")

	fileAjoined = sortWords(fileA)
	print("Непарний файл з відсортованими словами в кожному рядку: \n" + fileAjoined + "\n\n\n")

	fileBjoined = sortRows(fileB)
	print("Парний файл з відсортованими рядками: \n" + fileBjoined + "\n\n\n")

	fillFile("main.txt", mstr)
	fillFile("odd.txt", fileAjoined)
	fillFile("even.txt", fileBjoined)

def fillFile(name, value):
	myFile = open(name,"w")
	if not myFile:
		print("Не вдалося записати в файл " + name)
	else:
		myFile.write(value)
		myFile.close()

def enterFromKeyboard():
	print("Вводьте текст, в далі введіть пустий рядок:\n")
	result = ""
	inp = True
	while inp:
		inp = input("")
		result += ("" if result == "" else "\n") + inp
	return result

#	std::string str = ""
#	char ch
#	while ((ch = _getch()) != 27) {
#		std::cout << ch
#		if (ch == '\r') {
#			std::cout << '\n'
#			str += '\n'
#		} else if (ch == '\b') {
#			std::cout << ' ' << '\b'
#			str.pop_back()
#		} else {
#			str += ch
#		}
#	}
#	std::cout << "\n\n"
#	return str

def fillOtherFiles(myStr):
	fileA = []
	fileB = []
	pos = 0
	prev = 0
	toA = True
	while myStr.find('\n', prev) != -1:
		pos = myStr.find('\n', prev)
		if toA:
			fileA.append(myStr[prev:pos])
		else:
			fileB.append(myStr[prev:pos])
		prev = pos + 1
		toA = not toA
	if toA:
		fileA.append(myStr[prev:pos])
	else:
		fileB.append(myStr[prev:pos])
	return fileA, fileB

def sortWords(arr):
	result = ""
	for i in range(len(arr)):
		myStr = arr[i]
		words = []
		pos = 0
		prev = 0
		while myStr.find(' ', prev) != -1:
			pos = myStr.find(' ', prev)
			words.append(myStr[prev:pos])
			prev = pos + 1
		words.append(myStr[prev:pos])

		mySort(words)
		result += ("\n" if i > 0 else "") + myJoin(words, " ")
	return result

def mySort(arr):
	for i in range(len(arr)):
		k = i
		while k > 0 and arr[k] < arr[k - 1]:
			arr[k], arr[k-1] = arr[k-1], arr[k]
			k = k-1

def myJoin(arr, delim):
	result = ""
	for i in range(len(arr)):
		result += (delim if i > 0 else "") + arr[i]
	return result

def sortRows(rows):
	mySort(rows)
	return myJoin(rows, "\n")


main()
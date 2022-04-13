import struct
import math
from Globals import allFileName, openedFileName, Medicine, OpenedMedicine

def readAllMedicine():
    allMedicine = []

    file = 0
    try:
        file = open(allFileName, "rb")
    except IOError:
        print("Файл " + allFileName + " не знайдено!\n")
        return allMedicine

    content = file.read()
    i = 0
    end = len(content)
    while i < end:
        strLen = struct.unpack_from("i", content, i)[0]
        i+=4
        m = Medicine()
        m.name = struct.unpack_from(str(strLen)+"s", content, i)[0].decode("UTF-8")
        i+=math.ceil(strLen/4)*4
        m.hours = struct.unpack_from("i", content, i)[0]
        i+=4
        m.minutes = struct.unpack_from("i", content, i)[0]
        i+=4
        m.years = struct.unpack_from("i", content, i)[0]
        i+=4
        allMedicine.append(m)
        
    return allMedicine

def readOpenedMedicine():
    openedMedicine = []

    file = 0
    try:
        file = open(openedFileName, "rb");
    except IOError:
        print("Файл " + openedFileName + " не знайдено\n")
        return openedMedicine;


    content = file.read()
    i = 0
    end = len(content)
    while i < end:
        strLen = struct.unpack_from("i", content, i)[0]
        i+=4
        m = OpenedMedicine()
        m.name = struct.unpack_from(str(strLen)+"s", content, i)[0].decode("UTF-8")
        i+=math.ceil(strLen/4)*4
        m.openTimestamp = struct.unpack_from("i", content, i)[0]
        i+=4
        m.endTimestamp = struct.unpack_from("i", content, i)[0]
        i+=4
        openedMedicine.append(m)
    
    return openedMedicine

def resaveMedicine(m, m2):
    try:
        file = open(allFileName, "wb")
        for i in range(len(m)):
            tm = m[i]
            name = tm.name.encode("UTF-8")
            file.write(struct.pack("i"+str(len(name))+"s3i", len(name), name, tm.hours, tm.minutes, tm.years))
        file.close()
    except IOError:
        pass

    try:
        file2 = open(openedFileName, "wb")
        for i in range(len(m2)):
            tm = m2[i]
            name = tm.name.encode("UTF-8")
            file2.write(struct.pack("i"+str(len(name))+"s2i", len(name), name, tm.openTimestamp, tm.endTimestamp))
        file2.close()
    except IOError:
        pass

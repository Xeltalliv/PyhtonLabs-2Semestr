import struct
from Globals import allFileName, openedFileName, Medicine, OpenedMedicine

def inputAllMedicine(allMedicine):
    mode = input("Введіть R щоб перезаписати, чи щось інше щоб дописати: ")
    file = open(allFileName, ("w" if mode == 'r' or mode == 'R' else "a") + "b")

    inputLoop = True
    while inputLoop:
        mode = input("Введіть A щоб додати, чи щось інше щоб продовжити: ")

        if mode == 'a' or mode == 'A':
            m = Medicine()
            m.name = input("  Назва: ")

            timeList = input("  Час (ГГ:ХХ): ").split(":")

            m.years = int(input("  Років у закритому вигляді: "))

            m.hours = int(timeList[0])
            m.minutes = int(timeList[1])
            allMedicine.append(m)
            name = m.name.encode("UTF-8")
            file.write(struct.pack("i"+str(len(name))+"s3i", len(name), name, m.hours, m.minutes, m.years))
        else:
            inputLoop = False
    file.close()

def showAllMedicine(m):
    print("Кількість: " + str(len(m)) + "\n")
    for i in range(len(m)):
        print("  Назва: " + m[i].name)
        print("  Годин після відкриття: " + str(m[i].hours))
        print("  Хвилин після відкриття: " + str(m[i].minutes))
        print("  Років в закритому вигляді: " + str(m[i].years))
        print('\n')

def inputOpenedMedicine(dayTimestamp):
    mode = input("Введіть R щоб перезаписати, чи щось інше щоб дописати: ")
    file = open(openedFileName, ("w" if mode == 'r' or mode == 'R' else "a") + "b")

    inputLoop = True
    while inputLoop:
        mode = input("Введіть A щоб додати, чи щось інше щоб продовжити: ")

        if mode == 'a' or mode == 'A':
            m = OpenedMedicine()
            m.name = input("  Назва: ")

            timeList = input("  Час (ГГ:ХХ): ").split(":")
            m.openTimestamp = dayTimestamp + int(timeList[0]) * 60 + int(timeList[1])
            name = m.name.encode("UTF-8")
            file.write(struct.pack("i"+str(len(name))+"s2i", len(name), name, m.openTimestamp, m.endTimestamp))
        else:
            inputLoop = False
            
    file.close()

def showOpenedMedicine(m):
    print("Кількість: " + str(len(m)) + "\n")
    for i in range(len(m)):
        print("  Назва: " + m[i].name)
        timestamp1 = m[i].openTimestamp
        minutes = int(timestamp1 % 60)
        hours = int((timestamp1 / 60) % 24)
        day = int((timestamp1 / 60 / 24) % 365)
        year = int((timestamp1 / 60 / 24 / 365) + 1970)
        print("  Відкрито " + str(hours) + ":" + str(minutes) + " день " + str(day) + " року " + str(year))

        timestamp2 = m[i].endTimestamp
        minutes = int(timestamp2 % 60)
        hours = int((timestamp2 / 60) % 24)
        day = int((timestamp2 / 60 / 24) % 365)
        year = int((timestamp2 / 60 / 24 / 365) + 1970)
        print("  Кінець придатності " + str(hours) + ":" + str(minutes) + " день " + str(day) + " року " + str(year))
        print("")

def removeExpired(curTimestamp, m, m2):
    print("Перевірка придатності:")
    i = 0
    while i < len(m): #тут потрібно while а не for in range бо йде видалення елементів
        found = -1
        for j in range(len(m2)):
            if (m[i].name == m2[j].name):
                found = j

        if found == -1:
            print("  " + m[i].name + " не відкрито")
        else:
            m2[found].endTimestamp = m2[found].openTimestamp + m[i].minutes + m[i].hours * 60
            if m2[found].endTimestamp < curTimestamp:
                print("  У " + m[i].name + " скінчився срок придатності!")
                del m[i]
                del m2[found]
                i-=1
            else:
                print("  " + m[i].name + " відкрито")
        i+=1
    print("")


def inputTimeDate():
    print("Введіть теперішню дату і час:")
    curYear = int(input("  Рік: "))
    curDay = int(input("  День року: "))
    curHour = int(input("  Година: "))
    curMinute = int(input("  Хвилина: "))
    print("\n")
    curYear -= 1970
    curTimestamp = curMinute + curHour * 60 + curDay * 60 * 24 + curYear * 60 * 24 * 365
    dayTimestamp = curDay * 60 * 24 + curYear * 60 * 24 * 365
    return curMinute, curHour, curDay, curYear, curTimestamp, dayTimestamp

#!/usr/bin/env python

from Globals import allFileName, openedFileName, Medicine, OpenedMedicine
from Logic import calculateExpirationDates
from FileIO import readAllMedicine, readOpenedMedicine, resaveMedicine
from ConsoleIO import inputAllMedicine, showAllMedicine, inputOpenedMedicine, showOpenedMedicine, removeExpired, inputTimeDate

def main():
    curMinute, curHour, curDay, curYear, curTimestamp, dayTimestamp = inputTimeDate()

    m = readAllMedicine()
    print("\nСписок всіх ліків:")
    showAllMedicine(m)

    inputAllMedicine(m)
    m = readAllMedicine()

    m2 = readOpenedMedicine()
    calculateExpirationDates(m, m2)
    print("\nСписок відкритих ліків:")
    showOpenedMedicine(m2)

    m = readAllMedicine()
    m2 = readOpenedMedicine()
    removeExpired(curTimestamp, m, m2)
    resaveMedicine(m, m2)

    inputOpenedMedicine(dayTimestamp)

main()

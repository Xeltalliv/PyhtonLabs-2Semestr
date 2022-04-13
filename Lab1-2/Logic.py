from Globals import Medicine, OpenedMedicine

def calculateExpirationDates(m, m2):
    for i in range(len(m)):
        found = -1
        for j in range(len(m2)):
            if m[i].name == m2[j].name:
                found = j

        if found > -1:
            m2[found].endTimestamp = m2[found].openTimestamp + m[i].minutes + m[i].hours * 60

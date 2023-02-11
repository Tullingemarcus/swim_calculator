


def calculateTime(pace, num):
    time = 0
    min = 0
    sec = 0
    
    paceString = ""
    for letter in pace:
        if letter in ":":
            min = num * int(paceString)
            paceString = ""
        else:
            paceString += letter
    sec = num * int(paceString)
    newsec = int(sec / 60)
    min = min + newsec
    if min >= 60:
        newmin = min % 60
        if newmin <= 10:
            newmin = "0" + str(newmin)
        min = str(int(min/60)) + ":" + str(newmin)
    time = str(min) + ":" + str(sec % 60) 
    return time

    












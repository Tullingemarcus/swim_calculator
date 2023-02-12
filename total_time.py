def addTime(time1, time2):
    if time1 == "":
        time1 = "00:00:00"
    if time2 == "":
        time2 = "00:00:00"
    
    timeList = [None] * 6
    temp = ""
    i = 0
    for letter in time1:
        if letter == ":":
            temp = ""
            i += 1
        else:
            temp = temp + letter
            timeList[i] = temp

    temp = ""
    i += 1
    for letter in time2:
        if letter == ":":
            temp = ""
            i += 1
        else:
            temp = temp + letter
            timeList[i] = temp

    j = 0
    while j < 3:
        timeList[j] = int(timeList[j]) + int(timeList[j+3])
        j += 1

    sec = timeList[2]
    min = timeList[1]
    hour = timeList[0]
    
    secTemp = int(sec / 60)
    min = min + secTemp
    minTemp = int(min / 60)
    hour = hour + minTemp

    sec = sec % 60
    min = min % 60
    if sec < 10:
        sec = "0" + str(sec)
    if min < 10:
        min = "0" + str(min)
    if hour < 10:
        hour = "0" + str(hour)
    time = str(hour) + ":" + str(min) + ":" + str(sec)
    return time

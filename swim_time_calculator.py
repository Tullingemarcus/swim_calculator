#main function for doing the calculations
def calculateTime(hour,min,sec, num):
    #checks if hour,min and sec are empty
    if(hour == ""):
        hour = "00"
    if(min == ""):
        min = "00"
    if(sec == ""):
        sec = "00"

    #gets the value of each unit times the number of rounds
    sec = num * int(sec)
    min = num * int(min)
    hour = num * int(hour)

    #if sec or min are over 60 seconds/minutes we will get the equivalent for minutes/hour
    secTemp = int(sec / 60)
    min = min + secTemp
    minTemp = int(min / 60)
    hour = hour + minTemp

    #this takes out only the seconds if the seconds add up to more than a minute the minutes 
    # are stored in min
    sec = sec % 60
    #this takes out only the minutes if the minutes add up to more than an hour the hours 
    # are stored in hour
    min = min % 60
    #if any of the values are a single digit we add a zero in the front and string it
    if sec < 10:
        sec = "0" + str(sec)
    if min < 10:
        min = "0" + str(min)
    if hour < 10:
        hour = "0" + str(hour)
    #makes a string of the total time
    time = str(hour) + ":" + str(min) + ":" + str(sec)
    return time

#add two times together and return the total time
def addTime(time1, time2):
    #checks if time1 or time2 are empty
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

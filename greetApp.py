# This program greet user accoding to you.
# UserTime->it takes input time on which you want to greet
# Name->it takes name to which you want to greet
# Greeting-> it takes greeting to wish specified name


import datetime
UserTime = input("Enter time in \"hh:mm:ss\" format \n")
Name = input("Enter Name to Greet \n")
Date = input("Enter date in dd/mm/yy format \n")
Greeting = input("Enter greeting \n")

# return time in hh:mm:ss format


def genTime():
    x = datetime.datetime.now()

    localTime = x.strftime("%X")  # this function return local time format

    return localTime


# return date in dd:mm:yy format
def genDate():
    x = datetime.datetime.now()

    LocalDate = x.strftime("%x")  # this function return local time format
    return LocalDate

# this function show greeting
def greet(greeting, name, date): print(
    f" Very {greeting} {name} Today is {date} :) ")


print("Timer for greeting is set ...")


# This loop update time and date again again
while True:
    FormatedTime = genTime()

    FormatedDate = genDate()

    if (int(UserTime[0:2]) < int(FormatedTime[0:2])):
        print("your entered invalid time , Try again")
        break

    if (UserTime == FormatedTime and FormatedDate == Date):
        greet(Greeting, Name, Date)
        break

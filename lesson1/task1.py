# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

def getNameOfDay(day) :
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switch.get(day, "Wrong day!")

dayOfWeek = int(input ("Input the day of week\n"))
print (getNameOfDay(dayOfWeek))



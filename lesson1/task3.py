def getRange(quarter):
    switch = {
        1: "x > 0, y > 0",
        2: "x < 0, y > 0",
        3: "x < 0, y < 0",
        4: "x > 0, y < 0"
    }
    return switch.get(quarter, "Wrong quarter!")

quarter = int(input("Введите номер четверти (1-4) \n"))
print(getRange(quarter))
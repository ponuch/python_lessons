# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def printTable (x, y, z):
    print (f"x:{x}, y:{y}, z:{z}  ¬(X ∧ Y) ∨ Z = {bool(not(x and y) or z)}")

x = 0; y = 0;  z = 0
printTable(x, y, z)
x = 0; y = 0; z = 1
printTable(x, y, z)
x = 0; y = 1; z = 1
printTable(x, y, z)
x = 1; y = 1; z = 1
printTable(x, y, z)

x = 1; y = 0;  z = 0
printTable(x, y, z)
x = 1; y = 1; z = 0
printTable(x, y, z)
x = 0; y = 1; z = 0
printTable(x, y, z)


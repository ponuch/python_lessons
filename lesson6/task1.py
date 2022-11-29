# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN

n = int(input("Введите число N "))
tempStr = str(n)
result = n + int(tempStr * 2) + int(tempStr * 3)
print("Sum:", result)
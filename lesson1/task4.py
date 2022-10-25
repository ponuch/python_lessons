# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

def showNums(num):
    if num <= 0:
        raise ValueError("Неверный аргумент")
    for n in range(1, num):
        if n % 2 == 0:
            print(f'{n} ')
            
n = int(input("Введите n > 0\n"))
showNums(n)


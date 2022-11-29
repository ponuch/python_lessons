# Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.

import math

num = int(input("Input N > 0\n"))
list_nums = [math.factorial(n) for n in range(1, num + 1)]
print(list_nums)
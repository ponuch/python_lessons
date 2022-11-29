# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.

import random

def split(arr, size):
    arrs = []
    while len(arr) > size:
        item = arr[:size]
        arrs.append(item)
        arr = arr[size:]
    arrs.append(arr)
    return arrs

items = [random.randint(0, 9) for i in range(15)]
print(items)
print(split(items, 3))
n = int(input("Введите трёхзначное число \n"))

split_arr = split(items, 3)
arr_num = []

for arr_item in split_arr:
    num = int(''.join(map(str, arr_item)))
    arr_num.append(num)

print(arr_num)
    
result = arr_num.__contains__(n)
print("Contains:", result)

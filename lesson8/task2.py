# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random


# формируем данные
dim = random.randint(2, 6)

arr = [[random.randint(1, 5) for j in range(dim)] for i in range(dim)]

print(arr)


# Считаем сумму главной диагонали
sumMain = 0
for i in range(dim): 
    print(arr[i][i])
    sumMain += arr[i][i]
    
print("Main sum = {0}".format(sumMain))

# считаем сумму всех строк
sum_arr = []
for row in range(len(arr)):
    print(arr[row])
    sum_arr.append(sum(arr[row]))
    
print (sum_arr)

# result = list(filter(lambda x: x > sumMain, enumerate(sum_arr)))
result = [(idx, item) for idx, item in enumerate(sum_arr) if sum_arr[idx] > sumMain]

print("Result = {0}".format(result))

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа

import math

num = int(input("Input N > 0\n"))
format_str = '{:.' + str(num) + 'f}'
print(format_str.format(math.pi))
          
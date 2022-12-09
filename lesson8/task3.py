# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
31+30+31+31+30

import random

# формируем данные

class DayDesc:
    def __init__(self, temperature, month, day):
        self.temperature = temperature
        self.month = month
        self.day = day
        
    def __str__(self):
        return str(self.temperature) + " " + str(self.month) + " " + str(self.day)

arr = [[DayDesc(random.randint(1, 30), i, j) for j in range(31)] for i in range(5)]

res = [x for y in arr for x in y] # превращаем двумерный список в одномерный

sums = []

for idx in range(len(res)):
    print(idx)
    rng = res[idx:idx + 6]
    local_sum = 0
    for item in rng:
        local_sum += item.temperature
    
    sums.append(local_sum)
    
print("Minimum = {0}, maximum = {1}".format(min(sums), max(sums)))
    
    


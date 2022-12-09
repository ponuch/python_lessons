# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
31+30+31+31+30

import random
from operator import attrgetter

# формируем данные

class DayDesc:
    def __init__(self, temperature, month, day):
        self.temperature = temperature
        self.month = month
        self.day = day
        
    def __str__(self):
        return str(self.temperature) + " " + str(self.month) + " " + str(self.day)
    
    
class PeriodDesc:
    def __init__(self, temperature, start_month, start_day, end_month, end_day):
        self.temperature = temperature
        self.start_month = start_month
        self.start_day = start_day
        self.end_month = end_month
        self.end_day = end_day
        
    def __str__(self):
        return str(self.temperature) + " " + str(self.start_month) + " " + str(self.start_day) + " " + str(self.end_month) + " " + str(self.end_day)
        

arr = [[DayDesc(random.randint(1, 30), i, j) for j in range(31)] for i in range(5)]

res = [x for y in arr for x in y] # превращаем двумерный список в одномерный

sums = []

for idx in range(len(res)):
    rng = res[idx:idx + 6]
    local_sum = 0
    for item in rng:
        local_sum += item.temperature
    
    sums.append(PeriodDesc(local_sum, rng[0].month, rng[0].day, rng[-1].month, rng[-1].day))
    
min_period = min(sums, key=attrgetter('temperature'))
max_period = max(sums, key=attrgetter('temperature'))
    
print("Minimum = {0}, maximum = {1}".format(str(min_period), str(max_period)))
    
    


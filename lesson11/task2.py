import random
import numpy as np
import matplotlib.pyplot as plt

houses = {}
a=1

for i in range(0, 15):
    sq_house = random.randint(100, 300)
    price_house = random.randint(3, 20)
    houses[sq_house] = price_house * 1_000_000
    
# print(houses)

house_meter = {}
for key, value in houses.items():
    price_meter = value / key
    house_meter[key] = price_meter


    
result_data = {house:price for house, price in house_meter.items() if price < 50000}
print(dict(sorted(result_data.items())))
# выводим подходящие варианты в отсортированном виде
print(result_data)

# строим график по каждому дому с ценой квадратного метра
plt.bar(house_meter.keys(),house_meter.values())
plt.show()


# print(house_meter)
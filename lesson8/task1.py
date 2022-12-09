# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random
import statistics

#заполняем начальные данные
numOfGroups = random.randint(1, 5)
numOfPeople = random.randint(20, 30)
arrayOfEstimates = [[random.randint(1, 5) for j in range(numOfPeople)] for i in range(numOfGroups)]

print(arrayOfEstimates)

# считаем средний бал по группам
avg = []


for row in range(len(arrayOfEstimates)):
    print(row)
    print(arrayOfEstimates[row])
    avg.append(statistics.fmean(arrayOfEstimates[row]))
    
print(avg)
bestResult = max(avg)
groupNum = avg.index(bestResult)
print("Best group {0} with result {1}".format(groupNum, bestResult))
    

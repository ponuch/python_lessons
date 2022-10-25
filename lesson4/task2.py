# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. Выведите названия того товара, который закончился.

with open('/home/ponuch/Projects/Python_lessons/lesson4/ice.txt', encoding='utf-8') as data:
    ice_all = set(data.readline().split(','))
    ice = set(data.readline().split(','))
    print(ice_all)
    print(ice)
    print(ice_all.difference(ice))
    
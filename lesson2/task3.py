# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = 'one'
str2 = 'onetwonine'
dic = {}
for str in list(str1):
    dic[str] = str2.count(str)

print(dic)

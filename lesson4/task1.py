# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primes(num):
   i = 2
   primes = []
   while i * i <= num:
       while num % i == 0:
           primes.append(i)
           num = num / i
       i = i + 1
   if num > 1:
       primes.append(int(num))
   return primes

num = int(input("Input N > 0\n"))
print(primes(num))
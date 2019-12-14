import math, random

niceLine = """
=============
"""
print("Кастомизировать? (0 - нет, any - да)")
custom = int(input())
length = 0
minLength = 0
maxLength = 1
number = 0
divider = 1
minRange = 0
maxRange = 100
sort = 0
errorMes = False
if custom == 0:
    number = 5
    for _ in range(0, number):
        length = random.randint(4, 10)
        print(niceLine)
        print(length)
        for _ in range(0, length):
            a = random.randint(0, 100)
            print(a)
    print(niceLine)
else:
    print("Количество наборов:")
    number = int(input())
    print("Минимальная длина:")
    minLength = int(input())
    print("Максимальная длина:")
    maxLength = int(input())
    print("Минимальное значение:")
    minRange = int(input())
    print("Максимальное значение:")
    maxRange = int(input())
    print("Делитель:")
    divider = int(input())
    print("Сортировка (0 - нет, 1 - min_max, 2 - max_min):")
    sort = int(input())
    print(niceLine)
    for _ in range(0, number):
        length = random.randint(minLength,maxLength)
        print(length)
        result = []
        for _ in range(0, length):
            a = random.randint(minRange, maxRange)
            a = (a // divider) * divider
            for item in result:
                if a == item:
                    for _ in range(0, 10):
                        a = random.randint(minRange, maxRange)
                        a = (a // divider) * divider
                        if a != item:
                            continue
                if a == item:
                    errorMes = True
            result.append(a)
        if sort == 1:
            result.sort()
        if sort == 2:
            result.sort(reverse=True)

        for index in result:
            print(index)
        print(niceLine)
if errorMes:
    print("!: there are repeats in result. We tried to do our job, but maybe it is not your fucking day")
else:
    print("no repeats, that's cool btw")
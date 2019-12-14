import math, random

def quick_array(length=5): #output: array
    result = [length]
    for _ in range(0, length):
        a = random.randint(0, 100)
        result.append(a)

    return result

def quick_string(length=5): #output: multiline string
    result = [length]
    resultString = """"""
    for _ in range(0, length):
        a = random.randint(0, 100)
        result.append(a)
    for index in result:
        resultString += str(index) + "\n"
    return resultString


def custom_normal_array(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1): #output: unsorted array
    length = random.randint(minLength, maxLength)
    result = [length]
    for _ in range(0, length):
        a = random.randint(minValue, maxValue)
        a = (a // divider) * divider
        for item in result:
            if a == item:
                for _ in range(0, 10):
                    a = random.randint(minValue, maxValue)
                    a = (a // divider) * divider
                    if a != item:
                        continue
        result.append(a)

    return result

def custom_sorted_array(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1): #output: sorted (min-max) array
    length = random.randint(minLength, maxLength)
    result = []
    for _ in range(0, length):
        a = random.randint(minValue, maxValue)
        a = (a // divider) * divider
        for item in result:
            if a == item:
                for _ in range(0, 10):
                    a = random.randint(minValue, maxValue)
                    a = (a // divider) * divider
                    if a != item:
                        continue
        result.append(a)
    result.sort(reverse=False)
    result.insert(0,length)
    return result

def custom_sorted_reversed_array(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1): #output: sorted (max - min) array
    length = random.randint(minLength, maxLength)
    result = []
    for _ in range(0, length):
        a = random.randint(minValue, maxValue)
        a = (a // divider) * divider
        for item in result:
            if a == item:
                for _ in range(0, 10):
                    a = random.randint(minValue, maxValue)
                    a = (a // divider) * divider
                    if a != item:
                        continue
        result.append(a)
    result.sort(reverse=True)
    result.insert(0,length)
    return result

def custom_normal_string(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1): #output: multiline string
    length = random.randint(minLength, maxLength)
    result = [length]
    resultString = """"""
    for _ in range(0, length):
        a = random.randint(minValue, maxValue)
        a = (a // divider) * divider
        for item in result:
            if a == item:
                for _ in range(0, 10):
                    a = random.randint(minValue, maxValue)
                    a = (a // divider) * divider
                    if a != item:
                        continue
        result.append(a)

    for index in result:
        resultString += str(index) + "\n"
    return resultString

def custom_sorted_string(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1): #output: multiline sorted string
    length = random.randint(minLength, maxLength)
    result = []
    resultString = """"""
    for _ in range(0, length):
        a = random.randint(minValue, maxValue)
        a = (a // divider) * divider
        for item in result:
            if a == item:
                for _ in range(0, 10):
                    a = random.randint(minValue, maxValue)
                    a = (a // divider) * divider
                    if a != item:
                        continue
        result.append(a)
    result.sort(reverse=False)
    result.insert(0,length)
    for index in result:
        resultString += str(index) + "\n"
    return resultString

def custom_sorted_reversed_string(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1): #output: multiline sorted (rev) string
    length = random.randint(minLength, maxLength)
    result = []
    resultString = """"""
    for _ in range(0, length):
        a = random.randint(minValue, maxValue)
        a = (a // divider) * divider
        for item in result:
            if a == item:
                for _ in range(0, 10):
                    a = random.randint(minValue, maxValue)
                    a = (a // divider) * divider
                    if a != item:
                        continue
        result.append(a)
    result.sort(reverse=True)
    result.insert(0,length)
    for index in result:
        resultString += str(index) + "\n"
    return resultString
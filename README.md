# ege27InputGenerator
Создает входные данные для 27 задачи ЕГЭ по информатике
## Установка
Чтобы использовать модуль нужно скопировать файл input27gen.py в папку с проектом и импортировать его в проект

```python
import input27gen
```
## Использование
Модуль позволяет создавать разные наборы данных:
1) Случайный array
```python
quick_array(length=5)
```
2) Случайный string
```python
quick_string(length=5)
```
3) Кастомный array
```python
custom_normal_array(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1) #несортированный 
custom_sorted_array(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1) #сортированный (min-max)
custom_sorted_reversed_array(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1) #сортированный (max-min)
```
4) Кастомный string
```python
custom_normal_string(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1) #несортированный 
custom_sorted_string(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1) #сортированный (min-max)
custom_sorted_reversed_string(minLength = 5, maxLength=10, minValue=0, maxValue=100, divider=1) #сортированный (max-min)
```
## Входные данные
```python
length = 5 #Длина набора

minLength = 5 #Минимальная длина набора
maxLength = 10 #Максимальная длина набора 
minValue = 0 #Минимальное значение
maxValue = 100 #Максимальное значение
divider = 1 #Делитль
```

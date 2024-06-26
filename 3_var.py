# типы данных

# целочисленный тип данных (int, integer)
my_int = 123

# числа с плавающей точкой (вещественные числа) (float)
my_float = 123.1

# булевы значения (bool, boolean)
# в честь Джорджа Буля (булева алгебра)
# логическая 1
bool_1 = True
# логический 0
bool_2 = False

# строковые значения (символы, слова, тексты) (str, string)
my_char = 'A'
my_string = "python"
my_text = "мой какой-то текст"
multi_text = """много
строчный
текст"""
my_text = 'мой "текст" с кавычками'

# способы форматирования строк
str_1 = "температура котла = "
temp = 75.623451213123
str_2 = " *C"

# 1. Конкатенация (обьединение) строк - старый способ
result = str_1 + str(temp) + str_2

# 2. f-string (f-строка) - новый способ
result = f"{str_1}{temp:.2f}{str_2}"

# print(result)

# Арифметические операции

a = 2
b = 5

# сложение
result = a + b

# вычитание
result = a - b

# умножение
result = a * b

# обычное деление
# всегда возвращает число с плавающей точкой
result = a / b

# целочисленное деление
#  всегда возвращает целую часть результата
result = a // b

# деление по остатку
result = a % b

# возведение в степень
result = a ** b

# корень числа
import math
result = math.sqrt(100)

print(result)
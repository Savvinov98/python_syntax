# Циклы

# Оператор while

# Бесконечный цикл
# while True:
#     print("hello")

# бесконечный чикл с прерыванием
# while True:
#     val = input("Введите имя: ")
#     if val == "stop":
#         print("bye-bye!")
#         break
#     print(f"Привет, {val}")


# цикл с условием
# v0 = 0

# while v0 <= 10:
#     print(f"value = {v0}")
#     # инкремент (увеличение значение переменной)
#     # v0 = v0 + 1
#     # или
#     v0 += 1

# print("while is stopped")


# v1 = 10
# while v1 > -10:
#     print(f"value = {v1}")
#     # декремент
#     v1 -= 5


# пропуск части кода тела цикла
# v2 = -5
# while v2 < 15:
#     # 1 кусок кода
#     print(f"value = {v2}")
#     v2 += 1

#     if v2 <= 5:
#         continue

#     # 2 кусок кода
#     print(f"hello")



# оператор for

# 1. чтение значения обьекта с последовательностью
# 2. считанное значение присваивается в собственную переменную
# 3. выполняет код своего тела

# for v in "python":
#     print(v)

# lst0 = [10, 20, 30, 3, 300, 50, 2, 0]

# for val in lst0:
#     val *= 2
#     print(val)


# класс range()

r = range(10)
r = range(10, 20)
r = range(-10, 10, 2)

# print(r)

# for num in r:
#     print(num)

# for num in range(10, 20, 5):
#     print(num)

# безымянная переменная
# for _ in range(0, 10, 5):
#     print("hello")

dict_0 = dict(a=100, b=200, c=300)
print(dict_0)
# for _ in dict_0:
#     print(_)
# for _ in dict_0.values():
#     print(_)
for _ in dict_0.items():
    print(_)


# генератор списка (кортежа)
# генератор словаря
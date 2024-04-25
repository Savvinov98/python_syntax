# функции

# создание функции
# функция, обладающая параметрами и возвращающая значение
def func_1(par_0, par_1):
    res = par_0 ** par_1
    return res

def func_2(a, b=4):
    res = a * b
    return res

# вызов функции
# r = func_1(2, 8)
r = func_2(2)

# print(r)


# классы
# создание класса
class Cat:
    # метод-конструктор
    def __init__(self, n="Barsik", a=1):
        # атрибуты
        self.name = n
        self.age = a
        
    # метод экземпляра
    def mur(self):
        res = f"мур-мур! Меня зовут {self.name}, мне {self.age} лет"
        print(res)

# создание экземпляров (обьектов) класса Cat
c_0 = Cat("Murka", 3)
c_1 = Cat(a=5)

# вызов метода
c_0.mur()
c_1.mur()


# параметры функции
# ООП (наследование, полиморфизм, инкапсуляция)
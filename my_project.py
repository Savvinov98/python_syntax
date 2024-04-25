# Программа с графическим пользовательским интерфейсом (GUI)

# генератор паролей

# импортирование модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

# основная функция
def pwdGen(pwd_str: str):
    # кодирование в бай-строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование в обычную строку
    hex_str = hash_str.hexdigest()
    # возврат хеш-строки
    return hex_str[:10]

# обьект окна
app = Tk()

app.geometry("200x100")
app.title("Генератор пароля")

# обьекты для хранения строк
raw_pwd = StringVar()
result = StringVar()

# виджет текстовой метки
Label(text="Password:").grid(row=0, column=0)

# виджет поля ввода пароли
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# виджет кнопки 
def btn_func():
    result.set(pwdGen(raw_pwd.get()))
Button(text="START", command=btn_func).grid(row=1, column=0)

# виджет поля вывода пароли
Entry(textvariable=result).grid(row=1, column=1)

# точка входа программы
app.mainloop()
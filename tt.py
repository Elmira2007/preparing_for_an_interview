# 1.Создайте строку с вашим именем и фамилией.Выведите только ваше имя.
# Выведите ваше имя в верхнем регистре.Посчитайте количество символов в вашем имени и фамилии вместе.
#  full_name = "Пак Чимин"
# first_name = full_name.split()[0]
# # print("Имя:", first_name)

# upper_case_name = first_name.upper()
# print("Имя в верхнем регистре:", upper_case_name)

# total_characters = len(full_name.replace(" ", ""))
# print("Количество символов в имени и фамилии:", total_characters)

# 2.Создайте список чисел от 1 до 5.Добавьте число 6 в конец списка.
# Умножьте каждый элемент списка на 2.
# num = [1, 2, 3, 4, 5]
# num.append(6)

# doubled_num = [x * 2 for x in num]
# print("Список после добавления 6:", num)
# print("Список после умножения на 2:", doubled_num)

# 3.Запросите у пользователя ввод числа.Проверьте, является ли число четным или нечетным.
# Выведите соответствующее сообщение.
# user_number = int(input("Введите число: "))
# if user_number % 2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")

# 4.Создайте функцию, которая принимает два аргумента (числа) и возвращает их сумму.
# Вызовите функцию с двумя числами и выведите результат.
# def numbers(a, b):
#     return a + b

# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))

# result = numbers(number1, number2)
# print("Сумма чисел", number1, "и", number2, "равна", result)

# 5.Запросите у пользователя ввод числа.Если число больше 10, выведите "Число больше 10".
# Иначе выведите "Число не больше 10".
# user_number = int(input("Введите число: "))

# if user_number > 10:
#     print("Число больше 10") 
# else:
#     print("Число не больше 10")

# 6.Создайте класс "Person" с атрибутами "имя" и "возраст".
# Создайте объект этого класса с вашими данными и выведите информацию о себе.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}")

# my_info = Person("Чонгук", "26")
# my_info.info()

# 7.Создайте текстовый файл и напишите в нем несколько строк текста.Откройте файл, прочитайте строки и выведите их на экран.
# file_path = "tt.txt"

# with open(file_path, "w") as file:
#     file.write("Это первая строка текста.\n")
#     file.write("А это вторая строка текста.\n")
#     file.write("И еще одна строка для примера.\n")

# with open(file_path, "r") as file:
#     content = file.read()
#     print("Содержимое файла:")
#     print(content)

# 8.Импортируйте модуль random.Создайте список из нескольких целых чисел.
# Используйте функцию random.choice() для выбора случайного числа из списка.
# import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# random_number = random.choice(numbers)
# print("Случайное число из списка:", random_number)

# 1) Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Выведите с помощью lambda функции чётные числа с списка

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = list(filter(lambda x: x % 2 == 0, numbers))
# print(num)

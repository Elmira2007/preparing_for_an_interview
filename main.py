# 1 Какие типы данных есть в python. И какие изменияемые и не изм  

# int 
# str 
# float
# bool 

# set 
# frozenset 
# list 
# dict
# tuple
# ########################################################################

# 2 Принципы ООП 

# Наследование - мы принимаем параметры для дочернего класса от род.класса  
# Инкапцуляция - это для защиты нашего кода 
# Палиморфизм - принимаем параметры от род класса к дочернему и в нем же изменияем  
# Абстракция - Абстракция используется, чтобы скрыть внутренние характеристики функции от пользователей


# 3 Что такое inline кнопки в aiogram ?

# Это те кнопки которые появляються как сообщение
#########################################################################

#4 Что такое django ORM ? 

# Обработчик бд 

#########################################################################

# 5 авто документация DRF ? 

#swagger 
#redoc


#########################################################################

# 6 Типы HTTP-запросов 


# GET — получение ресурса
# POST — создание ресурса
# PUT — обновление ресурса
# DELETE — удаление ресурсаx

#########################################################################


# 7 Зачем нужен Serializer.py 

# для ОБРАБОТКИ  данных в Json формате, в апишке 
#########################################################################


#8 за что отвечают папка templates и static в django проекте 

#templates - html файлы
#static - медиа и стили
#########################################################################



#9 Зачем нужен permissions.py  

# для защиты данных от пользователей 
# задать роли 

##################################################################


#10 Встроенные функции 
# print
# input
# min 
# max 
# sum 
# len
# range
# set 
# type
# reversed 


#10 что такое lambda ?

# Это анонимная функция которая сокрощает код

# Дается 2 строки "Aidana" и "Adilet" . 
# Вам нужно в результате получить смешанную
# строку из двух имен, буква за буквой.
# Результат: "AAiddialnea

# str1 = "Aidana"
# str2 = "Adilet"
# result = ""

# for i in range(max(len(str1), len(str2))):
#     if i < len(str1):
#         result += str1[i]
#     if i < len(str2):
#         result += str2[i]

# print(result)





# a = """Advertising companies say advertising is necessary and important. It informs people about
# new products. Advertising hoardings in the street make our environment colourful. And
# adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
# programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
# healthy products. And adverts in magazines give us ideas for how to look prettier, be
# fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad
# for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
# know we love our children and want to give them everything. So they use children’s ‘pester
# power’ to sell their products. Finally, consumers say, if there is advertising there must be
# rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
# money."""

# print(a.count('s'))


################################################################################

 ##############################   ДЕНЬ2   #######################################




#  Что такое класс models.Model в Django от которго мы наследуемся 

# встроенный абстрактный класс 
#  




# Что такое объектно-ориентированное программирование 
# (ООП) и какие основные концепции оно включает в себя?

# Объектно-ориентированное программирование (ООП) - это парадигма 
# программирования, основанная на концепции объектов,
# которые являются инстансами классов, и взаимодействии между ними.

# Чем отличается класс от объекта в Python?

# Класс - это шаблон или описание объекта, определяющий его атрибуты и методы.
# Объект - это конкретный экземпляр класса.

# Как создать класс в Python? Приведите пример.

# class Name:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         print(f"Привет {self.name} мне {self.age}")
              
# students = Name("Geeks", 18)



# Как создать объект (экземпляр) класса в Python?

# students = Name("Geeks", 18)
# students = info()

# Что такое атрибуты класса и как их определять? 

# артибуты - это переменные внутри класса

# Что такое методы класса? Какие бывают типы методов в Python?

# функция внутри класса называется методом

# 1) Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Выведите с помощью lambda функции чётные числа с списка

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = list(filter(lambda x: x % 2 == 0, numbers))
# print(num)



# 2) Напишите функцию где мы передаем через аргументы число n как целое
# integer, надо вывести целое число в перевернутом виде
# например: n = 27, тогда перевёрнутое n это 72 

# def integer(n):
#     rev_n = int(str(n)[::-1])
#     return rev_n

# n = 89
# result = integer(n)
# print(result)



# 3) Вывести на экран циклом пять строк из нулей, причем каждая строка
# должна быть пронумерована. Подсказка: Используйте функцию range()
# или enumerate()

# for i in range(1, 6):
#     print(f"{i}) 0")


# 1)Создайте класс с именем Employee.
# 2) У класса Employee должны быть следующие атрибуты (характеристики сотрудника):
# name (имя сотрудника)
# age (возраст сотрудника)
# position (должность сотрудника)
# salary (заработная плата сотрудника)


# class Employee():
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
    
#     def info(self):
#         print(f"Hello, my name is {self.name}, Im {self.age} years old, Im {self.position}, and my salary {self.salary}")


# qwerty = Employee("Kudbhon", 15, "Backend Developer", 100000000)
# qwerty.info()
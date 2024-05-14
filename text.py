# 1
# import random

# list = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# def first(list):
#     randomm = random.choice(list)
#     print(randomm)
#     with open("exam.txt", "w") as exam:
#         exam.write(randomm)


# first(list)

# # 2
# text = """# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# # has been the industry's standard dummy text ever since the 1500s, when an unknown
# # printer took a galley of type and scrambled it to make a type specimen book. It has
# # survived not only five centuries, but also the leap into electronic typesetting, remaining
# # essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""

# with open("text.txt", "w") as ex2:
#     ex2.write(text)

# ex2 = open("text.txt", "w")
# ex2.write(text)
# ex2.close

# 3
# with open("text.txt", "r") as ex2:
#     text = ex2.read()

# with open("wikipedia.txt", "w") as ex3:
#     ex3.write(text)

# 4
# class Four():
#     def __init__(self, long, height):
#         self.long = long
#         self.height = height
#     def model(self):
#         p = self.long + self.height
#         print(f"периметр :{p}")
#         s = self.long * self.height
#         print(f"площадь: {s}")
# four = Four(34, 55)
# four.model()



# 5
# def list():
    # lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
    # print(lst[::-1])

# 6 
# def time(hour, min, sec):
#     huor_sec = hour * 3600
#     min_sec = min *60
#     print(f"{hour} час в секунде - {huor_sec} \n {min} минута в секунде - {min_sec} \n {sec} секунда в секунде -{sec} ")

# Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано

# def count_words_occurrences(phrase):
#     """
#     Функция для подсчета количества использований каждого слова во фразе.

#     :param phrase: исходная фраза
#     :return: словарь с количеством использований каждого слова
#     """
#     words = phrase.split()  # Разбиваем фразу на слова
#     word_counts = {}  # Создаем пустой словарь для подсчета количества слов

#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1  # Увеличиваем счетчик, если слово уже встречалось
#         else:
#             word_counts[word] = 1  # Инициализируем счетчик, если это первое вхождение слова

#     return word_counts

# # Пример использования
# phrase = "Это пример пример пример фразы с несколькими повторяющимися словами"
# word_counts = count_words_occurrences(phrase)
# print("Количество повторений каждого слова в фразе:")
# for word, count in word_counts.items():
#     print(f"{word}: {count}")


# Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована. 1
# def print_numbered_zeros():
#     """
#     Функция для вывода на экран пяти строк из нулей с нумерацией.
#     """
#     for i in range(1, 6):
#         print(f"{i}: {'0' * 5}")

# # Вызов функции
# print_numbered_zeros()

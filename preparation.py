# 1
# import random

# def random_list(r_list):
#     choice = random.choice(r_list)
    
#     with open("test.txt", "w") as f:
#         f.write(choice)
    
#     return choice

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# result = random_list(language)
# print(result)

# 2
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

# # 4
# class Four():
#     def __init__(self, long, height):
#         self.long = long
#         self.height = height
#     def model(self):
#         p = self.long + self.height
#         print(f"периметр :{p}")
#         s = self.long * self.height
#         print(f"площадь: {s}")
# four = Four(35, 90)
# four.model()

# 5
# from reverse_list import reverse_list

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reversed_lst = reverse_list(lst)
# print(reversed_lst)

# 6
# from reverse_list import convert_to_seconds

# hours = 5
# minutes = 23
# seconds = 50  

# total_seconds = convert_to_seconds(hours, minutes, seconds)
# print(total_seconds)





# # Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано

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



# # Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. 
# # Например:“Money, money, money, it’s always sunny, in the richmen’s world”. money:
# # 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

# def count_word_occurrences(phrase):
#     """
#     Функция для подсчета количества использований каждого слова во фразе.

#     :param phrase: исходная фраза
#     :return: словарь с количеством использований каждого слова
#     """
#     # Разбиваем фразу на слова, убирая знаки препинания и приводим к нижнему регистру
#     words = phrase.lower().replace(",", "").replace(".", "").split()
    
#     word_counts = {}  # Создаем пустой словарь для подсчета количества слов

#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1  # Увеличиваем счетчик, если слово уже встречалось
#         else:
#             word_counts[word] = 1  # Инициализируем счетчик, если это первое вхождение слова

#     return word_counts

# # Пример использования
# phrase = "Money, money, money, it’s always sunny, in the richmen’s world"
# word_counts = count_word_occurrences(phrase)
# print("Количество повторений каждого слова в фразе:")
# for word, count in word_counts.items():
#     print(f"{word}: {count}")

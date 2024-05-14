import random

def ask_questions_randomly():
    questions = [
        "Какие типы данных есть в Python? И какие изменияемые и неизменяемые?",
        "Принципы ООП",
        "Что такое inline кнопки в aiogram?",
        "Что такое Django ORM?",
        "Автодокументация DRF?",
        "Типы HTTP-запросов",
        "Зачем нужен Serializer.py?",
        "За что отвечают папки templates и static в Django проекте?",
        "Зачем нужен permissions.py?",
        "Что такое lambda?",
        "Что такое асинхронная и синхронная функция?",
        "Что такое models.Model от которого мы наследуемся?",
        "Что такое миксины?",
        "Что такое магические методы?", 
        "Когда мы используем ТелеБот?", 
        "Библиотека aiogram",
        "Что такаое база данных",
        "Системы управлениями базами данных", 
        "Для чего нужен GitHub?", 
        "Что такое парсинг?",  
        "Что такое Django?",
        "Что такое фреймворк и чем она отличается от библиотек?",
        "Что такое декараторы?",
        "Что такое *args и **kwargs?",
        "Что такое функция?", 
        "Для чего мы используем dictionary?", 
        "Какие есть циклы в Python?",
        "Чем отличаются list,tuple и dictionary?",
        "Что такое set и frozenset и чем они отличаются?"
    ]

    random.shuffle(questions)

    responses = {}
    for question in questions:
        answer = input(question + " ")
        responses[question] = answer

    return responses

# Вызов функции для вопросов
responses = ask_questions_randomly()
print(responses)

# СПОКОЙНО 
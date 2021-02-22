questions = {
    "Как дела?" : "Хорошо",
    "Что делаешь?" : "Программирую",
    "Где учишься?" : "На курсах Learn Python",
}

while True:
    ask = input("Введите вопрос:")
    print(questions.get(ask))


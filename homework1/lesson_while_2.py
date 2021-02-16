questions = {
    "Как дела?" : "Хорошо",
    "Что делаешь?" : "Программирую",
    "Где учишься?" : "На курсах Learn Python",
}


def ask_user():
    while True:
        ask = input("Введите вопрос: ")
        for key in questions:
            if key == ask:
                print(questions.get(key))

ask_user()
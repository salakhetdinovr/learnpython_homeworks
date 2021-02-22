def hello_user():
    while True:
        question = input("Как дела?")
        if question == "Хорошо":
            print("Молодец!")
            break
        else:
            print("Давай еще попытку!")

hello_user()

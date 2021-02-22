def hello_user():
    while True:
        try:
            question = input("Как дела?")
        except KeyboardInterrupt:
            print("Пока")
            break
        if question == "Хорошо":
            print("Молодец!")
            break
        else:
            print("Давай еще")
        

hello_user()
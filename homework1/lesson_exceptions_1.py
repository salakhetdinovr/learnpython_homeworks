def hello_user():
    while True:
        try:
            question = input("Как дела?")
            if question == "Хорошо":
                print("Молодец!")
                break
            else:
                print("Давай еще")
        except KeyboardInterrupt:
            print("Пока")
            break

hello_user()
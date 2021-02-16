age = int(input("Введите возраст: "))

def definition_of_age(age):
    if 1 <= age <= 6:
        return "Ты еще в детском саду."
    elif 7 <= age <= 18:
        return "Ты учишься в школе."
    elif 19 <= age <= 24:
        return "Ты студент ВУЗа."
    elif age >= 24:
        return "На работу."

age_human = definition_of_age(age)
print(age_human)

age = int(input("Введите возраст: "))

def definition_of_age(age):
    if age <= 6:
        return "Ты еще в детском саду."
    if age <= 18:
        return "Ты учишься в школе."
    if age <= 24:
        return "Ты студент ВУЗа."
    if age >= 24:
        return "На работу."

age_human = definition_of_age(age)
print(age_human)
str_1 = input("Введите какое-нибудь слово: ")
str_2 = input("Введите еще одно слово: ")

def two_strings(str_1, str_2):
    if str_1.isdigit() or str_2.isdigit():
        return 0
    elif str_1 == str_2:
        return 1
    elif str_1 != str_2 and len(str_1) > len(str_2):
        return 2
    elif str_1 != str_2 and str_2 == 'learn':
        return 3


str_print = two_strings(str_1, str_2)
print(str_print)
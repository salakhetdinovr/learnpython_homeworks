def get_summ(one, two, delimister='&'):
    one = str(one)
    two = str(two)
    return one + delimister + two

p = get_summ("Learn", "python").upper()
print(p)
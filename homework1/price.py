def format_price(price):
    price = int(price)
    return "Цена: " + str(price) + " руб."

p = format_price(56.24)
print(p)
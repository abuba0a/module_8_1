def add_everything_up(a, b):
    try:
        result = a + b
    except:
        return str(a) + str(b)
    else:
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print(add_everything_up(5, 7))

a = 23
b = -23

def absolute_value(n):
    if n < 0:
        n = -n
    return n

if absolute_value(a) == absolute_value(b):
    print("Абсолютное значение", a, "и", b, "равны")
else:
    print("Абсолютное значение", a, "и", b, "различны")
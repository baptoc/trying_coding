def absolute_value(n):
    return abs(n)  # в Python есть встроенная функция abs()

try:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    
    if absolute_value(a) == absolute_value(b):
        print(f"Абсолютное значение {a} и {b} равны")
    else:
        print(f"Абсолютное значение {a} и {b} различны")
        
except ValueError:
    print("Ошибка: пожалуйста, введите числа!")
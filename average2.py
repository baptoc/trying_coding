sum = 0
print('Эта программа возьмет несколько чисел и усреднит их')
count =int(input("Сколько чисел вы хотите усреднить: "))
current_count = 0

while current_count < count:
    current_count = current_count + 1 
    print("Число", current_count)
    number = float(input("Введите число: "))
    sum = sum + number
    
print("Среднее значение составило:", sum / count)
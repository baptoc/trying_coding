count = 0   
sum = 0.0
number = 1 

print("Введите 0, чтобы выйти из цикла")

while number != 0:
    number = float(input("Введите число: "))
    if number != 0:
        count = count + 1 
        sum = sum + number
    if number == 0:
        print("Среднее значение составило:", sum / count)
        
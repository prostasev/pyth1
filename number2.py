# Ввод значений m и n
m = int(input("Введите значение m: "))
n = int(input("Введите значение n: "))

# Вычисление результата с использованием тернарного оператора
result = m // n if n != 0 and m % n == 0 else m * n

# Вывод результата
print("Результат:", result)
cities_input = input("Введите города через пробел: ")# Ввод списка городов в одну строчку
# Преобразование строки в список
cities_list = cities_input.split()
# Создание итератора
cities_iterator = iter(cities_list)
# Получение первых двух значений
first_city = next(cities_iterator, None)
second_city = next(cities_iterator, None)
# Вывод результатов
print("Первый город:", first_city)
print("Второй город:", second_city)
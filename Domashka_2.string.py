#1 Напишите код, который преобразует всю строку text в нижний регистр и удаляет пробелы с обоих концов.
# Результат сохраните в переменную result и выведите ее.
#Исходная строка: text = " ПРИВЕТ, МИР! "
text = " ПРИВЕТ, МИР! "
text_trimmed = text.strip()
result = text_trimmed.lower()
print(result)
#решение после советов дипсика
text = " ПРИВЕТ, МИР! "
result = text.strip().lower()
print(result)

#2 У вас есть переменные product (название товара) и price (его цена).
# Используйте f-строку, чтобы создать строку message вида: "Товар [название] стоит [цена] рублей."
#Исходные данные: product = "яблоки" price = 85
product = "яблоки"
price = 85
result = f"Товар {product} стоит {price} рублей."
print(result)

#3 Дана строка alphabet.
# Используя срезы, создайте новую строку result, которая содержит каждую вторую букву из первых восьми символов исходной строки.
#Исходная строка: alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = alphabet[:8:2]
print(result)

#4
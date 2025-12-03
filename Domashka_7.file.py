#Задача 1: Создай файл numbers.txt и запиши в него числа от 1 до 5, каждое с новой строки.
#with open ("numbers.txt", "w") as file:
#    file.write ("1\n2\n3\n4\n5")

#Задача 2: Прочитай и выведи на экран всё содержимое файла example.txt (предположим, он существует).
#with open ("example.txt", "r") as file:
#    line = file.read()
#    print(line)

#Задача 3: Используя конструкцию with, открой файл log.txt в режиме добавления и запиши в него строку:
# "Программа запущена."
#with open ("log.txt", "a") as file:
#    file.write(" Программа запущена.")

#Задача 4: Создай текстовый файл с именем numbers.txt.
# Запиши в него три числа (каждое с новой строки): 10, 20 и 30.
# После этого открой файл для чтения, прочитай все числа, вычисли их сумму и выведи результат на экран.
#эту я не смогла сама решить, но будет тут
#with open("numbers.txt", "w") as file:
#    file.write("10\n20\n30")
#
#with open("numbers.txt", "r") as file:
#    # Преобразуем каждую строку в int и сразу суммируем
#    sum_number = sum(int(line.strip()) for line in file)
#    print(sum_number)

#Задача 5 (Контекстный менеджер with)
#Создай файл greeting.txt и запиши в него одну строку: "Hello, World!".
# Сделай это обязательно с использованием контекстного менеджера with.
# После этого открой тот же файл для чтения (тоже используя with), прочитай его содержимое и выведи на экран.
#with open ("greeting.txt", "w") as file:
#    file.write("Hello World!")
#with open ("greeting.txt", "r") as file:
#    print(file.read())

#Задача 6 (Работа с файлами)
#Создай текстовый файл с именем products.txt.
#Запиши в него три продукта (каждый с новой строки): хлеб, молоко, яйца. Затем открой файл для добавления ("a")
#и добавь в конец файла еще один продукт: сыр.
#В конце открой файл для чтения, прочитай и выведи всё его содержимое на экран.
with open ("products.txt", "w") as file:
    file.write("хлеб,\nмолоко,\nяйца")
with open ("products.txt", "a") as file:
    file.write("\nсыр")
with open ("products.txt", "r") as file:
    print(file.read())




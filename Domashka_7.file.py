#Задача 1: Создай файл numbers.txt и запиши в него числа от 1 до 5, каждое с новой строки.
#with open ("numbers.txt", "w") as file:
#    file.write ("1\n2\n3\n4\n5")

#Задача 2: Прочитай и выведи на экран всё содержимое файла example.txt (предположим, он существует).
#with open ("example.txt", "r") as file:
#    line = file.read()
#    print(line)

#Задача 3: Используя конструкцию with, открой файл log.txt в режиме добавления и запиши в него строку:
# "Программа запущена."
with open ("log.txt", "a") as file:
    file.write(" Программа запущена.")
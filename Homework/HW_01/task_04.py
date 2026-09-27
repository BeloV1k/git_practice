# HW 01 — Задача 4. Цифры трёхзначного числа
# Решение пиши ниже.
number = int(input("Введите любое трёх значное число: "))
summ = number // 100 + number % 100 // 10 + number % 10
product = (number // 100) * (number % 100 // 10) * (number % 10)
print(f"Введенное число: {number}, сумма его цифр: {summ}, произведение его цифр: {product}")
#ну еще можно было сделать так:
#number = int(input("Введите любое трёх значное число: "))
#num1 = number // 100
#num2 = number % 100 // 10
#num3 = number % 10
#print(f"Введенное число: {number}, сумма его цифр: {num1+num2+num3}, произведение его цифр: {num1*num2*num3}")

# Пример фактического запуска программы:
PS C:\User\belok\git_practice\Homework\HW_01> python task_04.py
Введите любое трёх значное число: 145
Введенное число: 145, сумма его цифр: 10, произведение его цифр: 20
PS C:\User\belok\git_practice\Homework\HW_01>
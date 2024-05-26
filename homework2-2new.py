# Первая задача
first_number = int (input ("Введите первое число: "))
second_number = int (input ("Введите второе число: "))
third_number = int (input ("Введите третье число: "))
if first_number == second_number and second_number == third_number and first_number == third_number:
    print(3)
# Вторая задача
first_number = int (input ("Введите первое число: "))
second_number = int (input ("Введите второе число: "))
third_number = int (input ("Введите третье число: "))
if first_number == second_number or second_number == third_number or first_number == third_number:
    print(2)
# Третья задача
first_number = int (input ("Введите первое число: "))
second_number = int (input ("Введите второе число: "))
third_number = int (input ("Введите третье число: "))
if not first_number == second_number:
    print(0)
if not second_number == third_number:
    print(0)
if not first_number == third_number:
    print(0)

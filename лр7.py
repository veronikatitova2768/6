# Проверка на четность/нечетность
number = int(input("Введите целое число: "))

if number % 2 == 0:
    print(f"{number} - четное число.")
else:
    print(f"{number} - нечетное число.")

# Поиск максимума
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_number = num1

if num2 > max_number:
    max_number = num2

if num3 > max_number:
    max_number = num3

print(f"Максимальное число из {num1}, {num2} и {num3} - это {max_number}.")

# Вычисление факториала числа
number = int(input("Введите целое неотрицательное число: "))

factorial = 1

if number < 0:
    print("Факториал отрицательного числа не определен.")
elif number == 0:
    print("Факториал числа 0 равен 1.")
else:
    for i in range(1, number + 1):
        factorial *= i

    print(f"Факториал числа {number} равен {factorial}.")

# Проверка на простоту числа
number = int(input("Введите целое число больше 1: "))

is_prime = True

if number <= 1:
    print("Число должно быть больше 1.")
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} - простое число.")
else:
    print(f"{number} - составное число.")

# Таблица умножения
number = int(input("Введите число для вывода таблицы умножения: "))

print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# Палиндром
def is_palindrome(s):
    # Приводим строку к нижнему регистру и удаляем пробелы
    s = s.lower().replace(" ", "")
    # Удаляем знаки препинания
    s = ''.join(char for char in s if char.isalnum())
    # Проверяем, является ли строка палиндромом
    return s == s[::-1]

user_input = input("Введите строку для проверки на палиндром: ")

if is_palindrome(user_input):
    print("Это строка является палиндромом.")
else:
    print("Это строка не является палиндромом.")

# Подсчет гласных и согласных
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    num_vowels = sum(1 for char in s if char in vowels)
    num_consonants = sum(1 for char in s if char in consonants)
    
    return num_vowels, num_consonants

user_input = input("Введите строку для подсчета гласных и согласных: ")

vowels, consonants = count_vowels_consonants(user_input)
print(f"Количество гласных: {vowels}")
print(f"Количество согласных: {consonants}")

# Сумма элементов списка
def sum_of_list(lst):
    return sum(lst)

# Пример списка чисел
numbers = [20, 40, 20, 10, 10]

# Вывод суммы всех элементов списка
print(f"Сумма всех элементов списка {numbers}: {sum_of_list(numbers)}")

# Обратный порядок чисел
def reverse_order(n):
    for i in range(n, 0, -1):
        print(i)

number = int(input("Введите натуральное число: "))
reverse_order(number)

# FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

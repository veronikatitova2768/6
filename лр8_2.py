def reverse_number(num):
    """Функция переворачивает число."""
    return int(str(num)[::-1])

def is_palindrome(num):
    """Функция проверяет, является ли число палиндромом."""
    return str(num) == str(num)[::-1]

def process_numbers(numbers):
    """Функция переворачивает числа из списка и выводит новый список с перевернутыми числами."""
    reversed_numbers = []
    for num in numbers:
        reversed_num = reverse_number(num)
        if is_palindrome(num):
            print(f"Число {num} является палиндромом.")
        reversed_numbers.append(reversed_num)
    return reversed_numbers

# Пример использования функций
numbers = [465, 957, 194, 3002, 2333, 95]
reversed_numbers = process_numbers(numbers)
print("Список с перевернутыми числами:", reversed_numbers)

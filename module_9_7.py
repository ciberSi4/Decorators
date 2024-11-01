# Домашнее задание по теме "Декораторы"

def checking_the_number(number): # Проверяет, является ли число простым
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1): # Метод пробных делений (или тест делимости)
        if number % i == 0:
            return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Простое" if checking_the_number(result) else "Составное")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c): # Сложение трех чисел
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
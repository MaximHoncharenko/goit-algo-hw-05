def caching_fibonacci():
    # Створення словника для зберігання результатів обчислення чисел Фібоначчі
    cache = {}

    # Внутрішня функція fibonacci(n), яка обчислює n-те число Фібоначчі
    def fibonacci(n):
        # Перевірка, чи вже є значення в кеші
        if n in cache:
            return cache[n]
        
        # Обчислення числа Фібоначчі
        if n <= 1:
            result = n
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
        
        # Збереження обчисленого значення в кеші
        cache[n] = result
        return result

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
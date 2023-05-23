def find_unique_value(numbers):
    for el in numbers:
        if numbers.count(el) == 1:
            return el

print(find_unique_value(input("Введіть числа:")))

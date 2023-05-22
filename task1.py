from collections import Counter
def find_unique_value(numbers):
    for el in numbers:
        if numbers.count(el) == 1:
            return el

numbers = [2, 3, 3, 3]
print(find_unique_value(numbers))

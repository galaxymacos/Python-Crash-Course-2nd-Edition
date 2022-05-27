import random


def generate_lottery():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
    result = ''
    for i in range(4):
        result += random.choice(numbers)
    return result



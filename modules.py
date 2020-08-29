def addition(number1, number2):
    return number1 + number2


def subtruction(number1, number2):
    return number1 - number2


def divition(number1, number2):
    return number1 / number2


def multiplication(number1, number2):
    return number1 * number2


def find_max(numbers):
    max_number =numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

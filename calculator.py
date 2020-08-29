from modules import *


class My_caculator:
    def __init__(self, number_1, number_2):
        self.number1 = number_1
        self.number2 = number_2

    def do_add(self):
        return addition(self.number1, self.number2)

    def do_sub(self):
        return subtruction(self.number1, self.number2)

    def do_mult(self):
        return multiplication(self.number1, self.number2)

    def do_divide(self):
        return divition(self.number1, self.number2)


number1 = int(input("Enter number1 : "))
number3 = int(input("Enterb number ; "))

my_calculator = My_caculator(number1, number3)
print(my_calculator.do_add())
print(my_calculator.do_sub())
print(my_calculator.do_mult())
print(my_calculator.do_divide())

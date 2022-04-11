class Addition:
    def calAddition(self, a, b):
        print("Addition of two no is:", a + b)


class Substraction:
    def calSubstraction(self, a, b):
        print("Subtraction of two no is:", a - b)


class Multiplication:
    def calMultiplication(self, a, b):
        print("Multiplication of two no is:", a * b)


class Calculator(Addition, Substraction, Multiplication):
    def calDivision(self, a, b):
        print("Division of two no is:", a + b)
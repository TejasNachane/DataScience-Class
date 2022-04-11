x = abs(int(input("Insert any Number: ")))

factorial = 1

while x > 1:
    factorial *= x
    x -= 1
print("The result of Factorial =",factorial)
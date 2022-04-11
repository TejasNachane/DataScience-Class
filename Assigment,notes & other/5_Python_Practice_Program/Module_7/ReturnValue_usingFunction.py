def avg(num1, num2):
    x = (num1 + num2) / 2
    return x


y = int(input(" Insert First Value: "))
z = int(input(" Insert Second Value: "))

average = avg(y, z)
print(round(average, 2))
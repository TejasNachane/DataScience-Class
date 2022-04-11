print("Zero operation terminates program !")
while True:
    op = input("Choose operator(+, -, *, /): ")
    if op == "0":
        break
    if op in ('+', '-', '*', '/'):
        x = float(input("Enter the value of x = "))
        y = float(input("Enter the value of y = "))
        if op == '+':
            print("%.2f" % (x+y))
        elif op == '-':
            print("%.2f" % (x-y))
        elif op == '*':
            print("%.2f" % (x*y))
        elif op == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Error! Division by zero error...")
        else:
            print("Invalid operator! ")

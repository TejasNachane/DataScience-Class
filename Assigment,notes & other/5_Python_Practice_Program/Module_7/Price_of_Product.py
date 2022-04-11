products = {"Mango": 6.9, "Banana": 4.9, "Apple": 4.7}

for pro, price in products.items():
    print(pro, " = ", price)

cost = 0
while True:
    pro = input("Select Product (n = nothing): ")
    if pro == 'n':
        break
    qty = int(input("Number of Products? "))
    cost += products[pro]*qty

print("Price of Product(s): ", cost)
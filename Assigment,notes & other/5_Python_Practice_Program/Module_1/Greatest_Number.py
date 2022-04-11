x=int(input("Insert any Number: "))
y=int(input("INsert any Number: "))
z=int(input("Insert any Number: "))

print("The maximum number is:",end="")

if y<=x>=z:
    print(x)
elif x<=y>=z:
    print(y)
elif x<=z>=y:
    print(z)

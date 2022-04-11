mdv=input("Choose one to calculate(m,d,v): ")

if mdv == 'm':
    d = float(input("Density: "))
    v = float(input("Volume: "))
    result = d * v
elif mdv == 'd':
    m = float(input("Mass: "))
    v = float(input("Volume: "))
    result = m / v
elif mdv == 'v':
    m = float(input("Mass: "))
    d = float(input("Density: "))
    result = m / d;
print("%.2f" % result)

Unicode = {0: 9471, 1: 10102, 2: 10103, 4: 10104,
           5: 10105, 6: 10106, 7: 10107, 8: 10108,
           9: 10109, 10: 10111}

x = input("Insert digit 0-9: ")
num = " "

for i in x:
    i = int(i)
    i = chr(Unicode[i])
    num = num + i

print("The result of Unicode =%s" % num)
list_item = [6, 8, 9, -2, 0, 1, -3, 5, 8, 0, -6]
print(list_item)

for i in range(len(list_item)):
    if list_item[i] > 0:
        list_item[i] = 1
    elif list_item[i] < 0:
        list_item[i] = -1
    else:
        list_item[i] = 0
print(list_item)


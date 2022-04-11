from random import random

num = 20
list_item = [0]*num

for i in range(num):
    list_item[i] = int(random()*50)
print(list_item)

maxi = 1
my_length = 1
my_code = 0

for i in range(1, num):
    if list_item[i] > list_item[i-1]:
        my_length += 1
    else:
        if my_length > maxi:
            maxi = my_length
            my_code = i
        my_length = 1
print("The maximum length =",maxi)
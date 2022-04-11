from random import random

x = [int(random()*5) for i in range(20)]
print(x)

my_set = set(x)

highest = None
frequent = 0

for item in my_set:
    freq = x.count(item)

    if freq > frequent:
        frequent = freq
        highest = item
print(highest)
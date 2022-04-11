from random import random

row = 5
col = 10
matrix = []
for i in range(row):
    my_row = []
    for j in range(col):
        my_row.append(int(random()*50)+10)
    matrix.append(my_row)

for row in matrix:
    print(my_row)

num = int(input("Range of numbers(10-50): "))

print("Rows: ", end=' ')

for i in range(row):
    if num in matrix[i]:
        print(i, end=' ')
print()

print(" Columns", end=' ')
for j in range(col):
    for i in range(row):
        if matrix[i][j] == num:
            print(j, end=' ')
            break
print()

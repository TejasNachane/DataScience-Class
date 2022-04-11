from random import randint

row = 5
matrix = []

for i in range(row):
    my_row = []
    for j in range(row):
        my_row.append(randint(1,100))
        print("%4d" % my_row[j],end=' ')
    matrix.append(my_row)
    print()
print()

for i in range(row):
    x = matrix[i][i]
    matrix[i][i] = matrix[i][row-1-i]
    matrix[i][row-1-i] = x

for i in matrix:
    for j in i:
        print("%4d" %j, end=' ')
    print()
str = input(" Insert some text with punctuation marks: \n")

symbols = ['.', ',', ';', ':', '!', '?', '(',')']

list_item = str.split()

x = 0
for i in list_item:
    if i[-1] in symbols:
        list_item[x] = i[:1]
        i = list_item[x]
    if i[0] in symbols:
        list_item[x] = i[1:]
    x += 1

x = 0
while x < len(list_item):
    print(list_item[x], end=' ')
    x += 1
    if x%5 == 0:
        print()

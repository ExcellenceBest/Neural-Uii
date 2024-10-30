a = (input('Введите числа: '))
b = (input('Введите числа: '))
data = []
data2 = []
for i in b:
    if i.isdigit():
        data2.append(i)
for i in a:
    if i.isdigit() and i not in b:
        data.append(i)
print(data)

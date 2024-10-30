a = (input('Введите числа: '))
data = []
for i in a:
    if i.isdigit():
        data.append(i)
data = set(data)
print(data)

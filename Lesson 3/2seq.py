a = (input('Введите числа через запятую, точку с запятой, слэш (1,2,3 1;2;3 1/2/3), но'
           ' только какой то один 1,2;3/4 - так нельзя: '))
data = []
for i in a:
    if i.isdigit():
        data.append(i)
data = set(data)
print(data)

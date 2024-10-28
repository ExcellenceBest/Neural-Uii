data = {'А. С. Пушкина': 1799, 'И.В.Грозного': 1533, 'Гвидо ван Россума': 1956, 'И. Панфилова': 1893, 'А. Грибоедова': 1795}
start = True
while start:
    right, wrong = 0, 0
    for key in data.keys():
        x = int(input(f'Введите год рождения {key}:  '))
        if x == data[key]:
            right += 1
        else:
            wrong += 1
    print(f'Правильных ответов {right}\n'
          f'Процент правильных ответов {(right*100)/len(data)}%\n'
          f'Неправильных ответов {wrong}\n'
          f'Процент неправильных ответов {(wrong*100)/len(data)}%\n')
    question = input(f'Желаете сыграть еще? (да или нет):  ')
    if question == 'нет':
        start = False
    elif question == 'да':
        continue
    else:
        print('Ошибка ввода!')


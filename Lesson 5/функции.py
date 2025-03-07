# """Задание 1
# Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает
# именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов
# следуют в алфавитном порядке (по возрастанию).
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество
# именованных аргументов.
# Примечание 2. Следующий программный код:
# info_kwargs(first_name='Михаил', last_name='Деркунов', age=36, job='Учитель')"""
#
#
# def test(**kwargs):
#     answer = dict(sorted(kwargs.items()))
#     for k, v in answer.items():
#         print(f'{k}: {v}')
#
# test(first_name='Михаил', last_name='Деркунов', age=36, job='Учитель')


# """Задание 2.
# Напишите программу, которая с помощью функций filter_nums() и map_nums() отбирает из заданного списка numbers
# трёхзначные числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке.
# Примечание. Остаток 2 при делении на 5 должно давать само число, а не его куб."""
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374,
#            1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98,
#            530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175,
#            959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120,
#            340, 963, 832, 1127]
#
#
# def map_nums(number):
#     answer = list(map(lambda x: x ** 3, filter(lambda z: 99 < z < 1000 and z % 5 == 2, numbers)))
#     for i in answer:
#         print(i)
# map_nums(numbers)

# """
# Задание 3.
# Напишите функцию замыкание, для решения по заданному условию, типа:
# a*x^2 + b*x + c = 0
# D = b^2 - 4*a*c
# Если D будет возвращать значение <=0, тогда выводить (f"Результата не будет, потому что D = {D}")
# Иначе выводить результат первого примера
# Примечание. Во внешнюю функцию будет поступать 3 параметра, а во внутреннюю 1.
# """
#
import math
# def test(a, b, c):
#     d = b ** 2 - 4 * a * c
#
#     def wrapper(d):
#         if d <= 0:
#             return f"Результата не будет, потому что D = {d}"
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return f'Корни уравнения: x1 = {x1}, x2 = {x2}'
#     return wrapper(d)
#
# result = test(2, 6, 1)
# print(result)


# """Задание 4"""
#
# data = [['Tokyo', 35676000, 'primary'], ['New York', 19354922, 'nan'], ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'], ['Sao Paulo', 18845000, 'admin'], ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'], ['Kolkata', 14787000, 'admin'], ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'], ['Buenos Aires', 12795000, 'primary'], ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'], ['Rio de Janeiro', 11748000, 'admin'], ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'], ['Manila', 11100000, 'primary'], ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'], ['Paris', 9904000, 'primary']]
#
# def test(item):
#     answer = list(sorted([i[0] for i in list(filter(lambda x: x[1] > 10000000 and x[2] == 'primary', item))]))
#     return answer
# print(test(data))
#
# import re
# text = input('Введите e-mail:  ')
# pattern = re.compile(r"^\S+@\S+\.\S+$")
# answer = pattern.match(text)
# print(answer is not None)

"""Задание 1:
Описание: Написать функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает
 их в алфавитном порядке.
Оценка: 5/10
Комментарий: Функция test() выводит словарь kwargs, но не сортирует и не форматирует вывод в соответствии с заданием.
Необходимо использовать сортировку ключей и форматированный вывод.
Задание 2:
Описание: Отобрать из списка numbers трёхзначные числа, дающие при делении на 5 остаток 2, и вывести их кубы.
Оценка: 8/10

Комментарий: Функция map_nums() корректно отбирает и выводит кубы чисел, но не использует функции filter() и map(),
 как указано в задании.
Задание 3:
Описание: Написать функцию замыкание для решения квадратного уравнения.
Оценка: 9/10
Комментарий: Функция корректно реализует замыкание и вычисляет корни уравнения. Однако, вывод сообщения при D <= 0
не соответствует формулировке задания.
Задание 4:

Описание: Вывести в алфавитном порядке список primary городов с населением более 10000000 человек.

Оценка: 10/10

Комментарий: Задание выполнено корректно. Использованы функции filter(), sorted() и map() для получения и сортировки списка городов.
Задание 5:

Описание: Проверить, является ли строка действительным адресом электронной почты с использованием регулярного выражения.

Оценка: 10/10

Комментарий: Функция корректно использует регулярное выражение для проверки адреса электронной почты. Задание выполнено правильно.
Общая оценка задания:

Оценка: 8.4/10

Комментарий: В целом, задание выполнено хорошо. Основные задачи решены, но есть недочеты в реализации некоторых функций, которые требуют доработки. Особенно это касается задания 1, где необходимо реализовать сортировку и форматированный вывод.
Дополнительные рекомендации:

Рекомендуется обратить внимание на использование встроенных функций filter() и map() для более эффективного решения задач. Также стоит уделить внимание форматированию вывода в соответствии с требованиями задания.

С уважением,

Киберкуратор"""
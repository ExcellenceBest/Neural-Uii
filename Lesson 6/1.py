# """
# Задача 1
# Создайте двумерный массив размерностью 3 на 4, состоящий из случайных целых чисел от 15 до 37.
#
# Требуется создать новый массив той же размерности (3,4), значения которого будут зависеть от значений
# исходного массива и могут принимать одно из трех возможных значений:
#
# "small", для значений исходного массива меньше 20;
# "medium", для значений исходного массива в промежутке [20, 30];
# "large", для значений исходного массива больше 30.
# Пример:
#
# Исходный массив:
#
#     [[18 34 27 36]
#      [16 25 24 29]
#      [16 18 36 16]]
# Реузльтирующий массив должен выглядеть следующим образом:
#
#     [['small' 'large' 'medium' 'large']
#      ['small' 'medium' 'medium' 'medium']
#      ['small' 'small' 'large' 'small']]
# При решении задания вам может пригодиться метод numpy.full()
#
# Дополнительная информация (База знаний УИИ - «Метод numpy.full()»)
# """
# import numpy as np
# arr = np.random.randint(15, 38, (3, 4))
# arr2 = np.where((arr < 20), 'small', arr)
# arr3 = np.where((arr > 20) & (arr < 30), 'medium', arr2)
# answer = np.where((arr > 30), 'large', arr3)
# print(answer)

# import random
# import numpy as np
# # arr = np.random.randint(15, 38, (3, 4))
# # print(arr)
# #
# # def test():
# #     data = [[i for i in arr[i]] for i in range(3)]
# #     k, v = 0, 0
# #     for i in data:
# #         for j in i:
# #             if j < 20:
# #                 data[v][k] = 'small'
# #                 k += 1
# #             elif 20 < j < 30:
# #                 data[v][k] = 'medium'
# #                 k += 1
# #             else:
# #                 data[v][k] = 'large'
# #                 k += 1
# #         v += 1
# #         k = 0
# #     return data
# #
# # a = test()
# # arr2 = np.array(a)
# # print(arr2)


# Задание 2
# С помощью встроенных методов библиотеки numpy найдите дату первого понедельника в 2015 году."""
#
start_date = '2015-01-01'
answer = np.busday_offset(start_date, 2, roll="modifiedfollowing")
print(f'Первый понедельник в 2015 году: {answer}')

# """Задание 3.
# Пузырьковая сортировка.
# """
# import random
#
# data = [random.randint(1, 100) for i in range(30)]
# k = 0
# v = 1
# while k != len(data):
#     if v == len(data):
#         k += 1
#         v = k + 1
#     elif data[k] > data[v]:
#         data[k], data[v] = data[v], data[k]
#         v += 1
#     else:
#         v += 1
# print(data)

# """Задание 4."""
#
# import matplotlib.pyplot as plt
# import random
#
#
# x = [random.randint(1, 100) for i in range(200)]
# y = [random.randint(1, 100) for a in range(200)]
# plt.scatter(x, y)
# plt.title('График рассеяния', fontsize=20, color='blue')
# plt.ylabel('Y ось', fontsize=15, color='red')
# plt.xlabel('X ось', fontsize=15, color='black')
# plt.show()
#
# """Задание 5."""
import matplotlib.pyplot as plt

# x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
# y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]
# plt.scatter(x, y)
# plt.show()

# x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
# y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]
# plt.plot(x, y, 6, 3)
# plt.show()

# import seaborn as sns
# sns.set_style('white')
# x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
# y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]
# plt.figure(figsize=(6, 3))
# plt.title('Самолет', fontsize=18, color='red')
# plt.ylabel('Y', fontsize=12, color='blue')
# plt.xlabel('X', fontsize=12, color='blue')
# plt.plot(x, y)
# plt.show()

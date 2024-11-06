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
import random

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
# start_date = '2015-01-01'
# answer = np.busday_offset(start_date, 2, roll="modifiedfollowing")
# print(f'Первый понедельник в 2015 году: {answer}')

import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
# sns.set_style('darkgrid')

x = np.random.randint(1, 15, 3)
y = np.random.randint(1, 15, 3)
print(x)
print(y)
plt.scatter(x, y)

# plt.plot(x, y)
# plt.title('Наш первый график', fontsize=14, color='m')
# plt.ylabel('Y ось', fontsize=10, color='orange')
# plt.xlabel('X ось', fontsize=12, color='g')
plt.show()


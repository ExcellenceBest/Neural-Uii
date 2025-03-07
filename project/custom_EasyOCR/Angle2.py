# Установка библиотеки.
!pip - q
install
easyocr

import easyocr

pip
install
opencv - python

!python3 - m
pip
install
paddlepaddle - gpu

# ! pip uninstall -y pillow
%%capture
!pip
install
"paddleocr>=2.0.1"

from paddleocr import PaddleOCR, draw_ocr

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.

paddle_ocr_ru = PaddleOCR(use_angle_cls=True, lang='ru')

from paddleocr import PaddleOCR
import cv2

# Инициализация PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='ru')  # Используйте 'ru' для русского языка

# Загрузка изображения
image_path = 't.jpg'
image = cv2.imread(image_path)

# Распознавание текста
result = ocr.ocr(image, cls=True)

# Вывод результатов
for line in result:
    print(line)

print(len(line))

import math


def calculate_rotation_angle(line):
    # Координаты bounding box
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = line[0][0]

    # Вычисление угла наклона
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx) * 180 / math.pi
    return angle


# Пример для первой строки
angle = calculate_rotation_angle(result[0])
print(f"Угол поворота: {angle} градусов")


def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Матрица поворота
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated


# Поворот изображения
rotated_image = rotate_image(image, angle)  # Отрицательный угол для компенсации поворота

# Сохранение или отображение результата
cv2.imwrite('rotated_image.jpg', rotated_image)
# cv2.imshow('Rotated Image', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Распознавание текста
result = ocr.ocr('t.jpg', cls=True)

print(result[0])
print(result[0][0])
print(result[0][1])
print(result[0][2])
print(result[0][3])

import math
import cv2
import numpy as np


def calculate_rotation_angle(line):
    # Координаты bounding box
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = line

    # Вычисление угла наклона
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx) * 180 / math.pi
    print(angle)
    return angle


# def rotate_image(image, angle):
#     # Получаем размеры изображения
#     (h, w) = image.shape[:2]
#     # Вычисляем центр изображения
#     center = (w // 2, h // 2)
#     # Получаем матрицу поворота
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     # Применяем аффинное преобразование
#     rotated = cv2.warpAffine(image, M, (w, h))
#     return rotated

# def align_lines(image, lines):
#     aligned_images = []
#     for line in lines:
#         # Вычисляем угол поворота для текущей строки
#         angle = calculate_rotation_angle(line)
#         # Поворачиваем изображение на вычисленный угол
#         rotated_image = rotate_image(image, angle)  # Отрицательный угол для выравнивания
#         aligned_images.append(rotated_image)
#     return aligned_images

# # Пример использования
# # Предположим, что `result` содержит координаты bounding box для каждой строки
# # и `image` - это исходное изображение
# aligned_images = align_lines(image, result)

# Вывод угла поворота для первой строки
for i in result[0]:
    print(i[0], i[1])
    angle = calculate_rotation_angle(i[0])
    print(f"Угол поворота: {angle} градусов")

# # Сохранение или отображение выровненных изображений
# for i, aligned_image in enumerate(aligned_images):
#     cv2.imwrite(f"aligned_line_{i}.jpg", aligned_image)

import matplotlib.pyplot as plt

from paddleocr import PaddleOCR
import cv2

# Инициализация PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='ru')  # 'en' для английского языка, 'ru' для русского

# Загрузка изображения
image_path = 't.jpg'
image = cv2.imread(image_path)

# Распознавание текста
result = ocr.ocr(image, cls=True)

# import numpy as np
# for line in result:
#     for word in line:
#         # Координаты bounding box
#         box = word[0]  # Координаты четырех углов прямоугольника

#         # Преобразуем координаты в формат, подходящий для cv2.rectangle
#         box = [tuple(map(int, point)) for point in box]  # Преобразуем в целые числа
#         print(box)
box = [(64, 409), (696, 263), (704, 297), (73, 448)]
# Рисуем рамку вокруг слова
cv2.polylines(image, [np.array(box)], isClosed=True, color=(0, 255, 0), thickness=2)

# Сохраняем или отображаем изображение с рамками
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)  # Сохраняем изображение

import math
import cv2
import numpy as np


def calculate_rotation_angle(line):
    # Координаты bounding box
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = line

    # Вычисление угла наклона
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx) * 180 / math.pi
    print(angle)
    return angle


angle = calculate_rotation_angle(box)
print(f"Угол поворота: {angle} градусов")


def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Матрица поворота
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated


# Поворот изображения
rotated_image = rotate_image(image, angle)  # Отрицательный угол для компенсации поворота

# Сохранение или отображение результата
cv2.imwrite('rotated_image.jpg', rotated_image)

# Распознавание текста
result = ocr.ocr('rotated_image.jpg', cls=True)

print(result)
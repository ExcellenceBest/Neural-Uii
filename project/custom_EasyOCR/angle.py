# Установка библиотеки.
!pip -q install easyocr

import easyocr

pip install opencv-python
!python3 -m pip install paddlepaddle-gpu
# ! pip uninstall -y pillow
%%capture
!pip install "paddleocr>=2.0.1"

from paddleocr import PaddleOCR, draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.

paddle_ocr_ru = PaddleOCR(use_angle_cls=True, lang='ru')

from paddleocr import PaddleOCR
import cv2
# Инициализация PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Используйте 'ru' для русского языка

# Загрузка изображения
image_path = '9.jpg'
image = cv2.imread(image_path)

# Распознавание текста
result = ocr.ocr(image, cls=True)

# Вывод результатов
for line in result:
    print(line)

import math


def calculate_rotation_angle(line):
    # Координаты bounding box
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = line[16][0]

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
cv2.waitKey(0)
cv2.destroyAllWindows()


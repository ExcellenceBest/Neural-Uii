# # !pip -q install easyocr
#
import easyocr
# import shutil
# import os
# import random
# from PIL import ImageEnhance, ImageFilter, Image
# import cv2
# from google.colab.patches import cv2_imshow
# import matplotlib.pyplot as plt
# import numpy as np

reader = easyocr.Reader(['ru'],
                        model_storage_directory='custom_EasyOCR/model',
                        user_network_directory='custom_EasyOCR/user_network',
                        recog_network='custom_example')

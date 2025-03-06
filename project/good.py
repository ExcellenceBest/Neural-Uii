import re


def get_text(path: str) -> dict:
    base = {'глюкоза': r'глюко', 'креатинин': r'креати', 'мочевина': r'мочеви', 'альбумин': r'альбум', 'глобулин': r'глобул'}
    dct = {}
    with open(path, 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file.readlines()]
        string = ''
        for i in data:
            string += i + ' '
        print(string)
        string1 = string.split()
        print(string1)
    for key in base:
        d = base[key]
        k = key
        [print(string1[i]) for i in range(len(string1)) if d in string1[i]]
        dct[k] = 1
    return dct


path = 'text.txt'
data = get_text(path)
print(data)


# from keras.models import load_model
# model.save('model.h5')
# # Загрузка обученной модели
# loaded_model = load_model('model.h5')

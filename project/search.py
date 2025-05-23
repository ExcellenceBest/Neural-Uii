
"""Функция для проверки возможности конвертации строки в число с плавающей точкой """
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

"""Функция для поиска заданных слов и значений, основывается на поиске слова и 
первого последующего за словом числового значения"""
def get_text(path: str) -> dict:
    """База слов и фрагментов заданных для поиска слов в тексте распознанном НС"""
    base = {'глюкоза': 'глюко', 'креатинин': 'креати', 'мочевина': 'мочеви',
            'альбумин': 'альбум', 'глобулин': 'глобул', 'AST': 'азт', 'ALT': 'ац'}
    dct = {}
    """Контекстный менеджер для чтения текстового файла"""
    with open(path, 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file.readlines()]
        string = ''
        """Перевод всего текста в нижний регистр"""
        for i in data:
            string += i.lower() + ' '
        """Конвертация в список"""
        string = string.split()
        ind = []
        for key in base:
            d = base[key]
            for index, element in enumerate(string):
                if d in element:
                    ind.append(index)
                    for _ in range(index, len(string)):
                        string[_] = string[_].replace(',', '.')
                        if is_number(string[_]):
                            ind.append(string[_])
                            dct[key] = string[_]
                            break
                        else:
                            continue
                    break
                else:
                    continue
        return dct

path = 'text.txt'
answer = get_text(path)
print(answer)

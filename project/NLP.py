def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_text(path: str) -> dict:
    base = {'глюкоза': r'глюко', 'креатинин': r'креати', 'мочевина': r'мочеви',
            'альбумин': r'альбум', 'глобулин': r'глобул'}
    dct = {}
    with open(path, 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file.readlines()]
        string = ''
        for i in data:
            string += i + ' '
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

path = 'txt2.txt'
answer = get_text(path)
print(answer)

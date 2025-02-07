import re


def get_text(path: str) -> dict:
    base = {'глюкоза': r'глюко', 'креатинин': r'креати', 'мочевина': r'мочеви', 'альбумин': r'альбум', 'глобулин': r'глобул'}
    dct = {}
    with open(path, 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file.readlines()]
        print(data)
        string = ''
        for i in data:
            string += i + ' '
        print(string)
        string1 = string.split()
        print(string1)




        # for key in base:
        # #
        #     d = base[key]
        #     k = key
        #     print([s for s in string.split(" ") if d in string])
            # [print(string1[i]) for i in range(len(string1)) if d in string1[i]]
            # res = re.split(d, string)
            # result = res[1] if len(res) > 1 else ""
            # print(result)
        abc = []
        ind = []
        for key in base:
            d = base[key]
            [abc.append(string1[i]) for i in range(len(string1)) if d in string1[i]]
            for index, element in enumerate(string1):
                if d in element:
                    ind.append(index)
                    for _ in range(index, len(string1)):
                        if string1[_].isdigit():
                            print(string1[_])
        # k = 0
        # for _ in range(ind[k], len(string1)):
        #     if _.isdigit():
        #         k.append(int(_))





                    # for _ in range(index, len(string1)):
                    #     if string1[_].isdigit():
                    #         print(string1[index+1])
                    #         abc.append(string1[index+1])
                    #
                    #         break
        # print(abc)
        # print(ind)
        # q = [(i, c) for i, c in enumerate(string) if c.isdigit()]
        #
        # score = score.split(' ', 1)[0]
        # dct[key] = score

        return dct

path = 'text.txt'
data = get_text(path)

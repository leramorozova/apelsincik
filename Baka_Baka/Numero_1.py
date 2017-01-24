import re

def step_1(file_name):
    file = open(file_name, 'r', encoding='UTF-8')
    file = file.read()
    return file


def step_2(step_1_result):
    text = step_1_result
    text = text.lower()
    text = re.sub('[«…:,—?!.\t»~]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub('  ', ' ', text)
    text = text.split()
    return text


def step_3():
    block = step_2(step_1(file_name))
    d = {}
    for word in block:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


def step_4(d):
    d_invert = {}
    for k, v in iter(d.items()):
        d_invert.setdefault(v, []).append(k)
    num = len(d_invert.keys())
    best_word = d_invert[max(d_invert)]
    for word in best_word:
        print('Самое частотное слово в тексте: "' + word + '" набравшее ' + str(max(d_invert)) + ' вхождений.\n')
    return num


def step_5(num, block):
    num_2 = len(block)
    final_num = num_2 / num
    print('Среднее значение частотности слов в тексте: ' + str(final_num))


if __name__ == '__main__':
    file_name = input('Введите имя файла с текстом: ')
    step_5(step_4(step_3()), step_2(step_1(file_name)))
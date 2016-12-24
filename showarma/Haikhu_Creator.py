import random

def open_file():
    FTO = open('slovar.txt', 'r', encoding='UTF-8')
    WORDS = FTO.readlines()
    FTO.close()
    return WORDS

def find_word(WORDS):
    WORD_PREV = random.choice(WORDS)
    WORD = WORD_PREV.strip('\n')
    #print (WORD)
    return WORD

def counter(WORD):
    i = 0
    GLASS = 'ouieayáíéóú'
    for PART in WORD:
        if PART in GLASS:
            i += 1
    #print(i)
    return i

def line_1_creator(SLOG_COUNT):
    I_MAX = SLOG_COUNT
    BLOCK = []
    while I_MAX >= 0:
        WORD = find_word(open_file())
        I = counter(WORD)
        I_MAX -= I
        if I_MAX > 0:
            BLOCK.append(WORD)
            continue
        elif I_MAX == 0:
            BLOCK.append(WORD)
            break
        elif I_MAX < 0:
            BLOCK = []
            I_MAX = SLOG_COUNT
            continue
    BLOCK = ' '.join(BLOCK)
    print (BLOCK)

def main():
    I = 1
    while I == 1:
        TEXT = input(' Для запуска создания генератора Хайку, нажмите Enter, оставив поле пустым. Или введите любой символ, чтобы выйти из программы:   ')
        while TEXT == '':
            print('\nВот, что удалось создать в этот раз ^^ \n')
            line_1_creator(5)
            line_1_creator(7)
            line_1_creator(5)
            CHECK = input('\nЧтобы создать еще одну Хайку (Или как правильно...) нажмите Enter, оставив поле пустым: ')
            if CHECK == '':
                TEXT = ''
            else:
                TEXT = 'Sometext'

        else:
            print('\nでは、また。先輩。')
            I = 2

if __name__ == '__main__':
    main()
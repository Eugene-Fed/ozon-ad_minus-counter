# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

minus_words = pd.read_csv('minus_words.csv', sep=',')  # столбцы: minus_words, count
ad_stat = pd.read_csv('ad_stat.csv', sep=';')
# столбцы SKU, Название товара, Поисковая фраза, *Запрос пользователя*, *Показы*, *?Клики, CTR (%), Расход (руб., с НДС)


def get_word_base(target_word=''):
    """Функция получает на входе слово и выдает его 'корень', или точнее слова без суффикса или окончания.
    Это необходимо, чтобы учесть все словоформы указанных минус-слов при дальнейшем поиске среди пользовательски фраз"""
    WORD_LEN = len(target_word)              # дабы не заставлять Python каждый раз считать длину строки

    # Далее мы выделяем корень минус-слов, чтобы учесть все подходящие словоформы в минус-фразах
    # Для этого необходимо вычесть из слова определенное количество символов с конца. У длинных слов - окончание длиннее
    # TODO убрать minus_word_ending, т.к. это исключительно для самопроверки на время тестов
    if WORD_LEN > 6 and target_word[-1] == 'ь':  # у слов > 6 знаков и с 'ь' на конце - суффикс обычно длиннее
        target_word = target_word[:-3]
    elif WORD_LEN > 4:
        target_word = target_word[:-2]        # у длинных слов без "ь" на конце - убираем суффикс или окончание
    elif WORD_LEN > 3:
        target_word = target_word[:-1]        # у коротких слов суффикс часто нулевой, а окончание - короткое
    # если длина слова до 3 символов включительно, то мы ничего от него не отрезаем

    return target_word


def search_word_in_phrases(minus_word=''):

    pass


for i, row in minus_words.iterrows():       # i - индекс, row - все остальные данные в строке
    # получаем значение столбца 'minus_words' из каждой строки ДатаФрейма
    minus_word = get_word_base(str(row['minus_words']))

    print(minus_word)

# print('Таблица минус-слов')
# print(minus_words.head())
print('\n\nТаблица со статистикой')
print(ad_stat.head(5)[['Запрос пользователя', 'Показы']])
# input("Press 'Enter'")

# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

minus_words = pd.read_csv('minus_words.csv', sep=',')  # столбцы: minus_words, count
ad_stat = pd.read_csv('ad_stat.csv', sep=';')
# столбцы SKU, Название товара, Поисковая фраза, *Запрос пользователя*, *Показы*, *?Клики, CTR (%), Расход (руб., с НДС)

for i, row in minus_words.iterrows():       # i - индекс, row - все остальные данные в строке
    minus_word = str(row['minus_words'])    # получаем значение столбца 'minus_words' из каждой строки ДатаФрейма
    minus_word_ending = ''                             # окончание для проверки на время тестов
    WORD_LEN = len(minus_word)              # дабы не заставлять Python каждый раз считать длину строки

    # Далее мы выделяем корень минус-слов, чтобы учесть все подходящие словоформы в минус-фразах
    # Для этого необходимо вычесть из слова определенное количество символов с конца. У длинных слов - окончание длиннее
    # TODO: убрать minus_word_ending, т.к. это исключительно для самопроверки на время тестов
    if WORD_LEN > 6 and minus_word[-1] == 'ь':  # слов > 6 знаков и с 'ь' на конце - суффикс обычно длиннее
        minus_word_ending = minus_word[-3:]     # todo: УБРАТЬ
        minus_word = minus_word[:-3]
    elif WORD_LEN > 4:
        minus_word_ending = minus_word[-2:]     # todo: УБРАТЬ
        minus_word = minus_word[:-2]        # у длинных слов без "ь" на конце - убираем суффикс или окончание
    elif WORD_LEN > 3:
        minus_word_ending = minus_word[-1:]     # todo: УБРАТЬ
        minus_word = minus_word[:-1]        # у коротких слов суффикс часто нулевой, а окончание - короткое
    # если длина слова до 3 символов включительно, то мы ничего от него не отрезаем

    print('Минус фраза: "{}", окончание: "{}"'.format(minus_word, minus_word_ending))

# print('Таблица минус-слов')
# print(minus_words.head())
print('\n\nТаблица со статистикой')
print(ad_stat.head(5)[['Запрос пользователя', 'Показы']])
# input("Press 'Enter'")

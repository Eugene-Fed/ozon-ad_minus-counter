# -*- coding: UTF-8 -*-

import pandas as pd
import os.path

MINUS_FILE = 'data/minus_words.csv'
STAT_FILE = 'data/ad_stat.csv'

# Проверяем наличие файлов данных. В случае их отсутствия - используем тестовые данные.
if not os.path.exists('data/minus_words.csv'):
    MINUS_FILE = 'data/minus_words_sample.csv'
if not os.path.exists('data/ad_stat.csv'):
    STAT_FILE = 'data/ad_stat_sample.csv'

minus_words = pd.read_csv(MINUS_FILE, sep=',')  # столбцы: minus_words, count
ad_stat = pd.read_csv(STAT_FILE, sep=';')
# столбцы: SKU, Название товара, Поисковая фраза, *Запрос пользователя*, *Показы*, Клики, CTR (%), Расход (руб., с НДС)


def get_word_base(target_word=''):
    """Функция получает на входе слово и выдает его 'корень', или точнее слова без суффикса или окончания.
    Это необходимо, чтобы учесть все словоформы указанных минус-слов при дальнейшем поиске среди пользовательски фраз"""
    WORD_LEN = len(target_word)              # дабы не заставлять Python каждый раз считать длину строки

    # Далее мы выделяем корень минус-слов, чтобы учесть все подходящие словоформы в минус-фразах
    # Для этого необходимо вычесть из слова определенное количество символов с конца. У длинных слов - окончание длиннее
    if WORD_LEN > 6 and target_word[-1] == 'ь':  # у слов > 6 знаков и с 'ь' на конце - суффикс обычно длиннее
        target_word = target_word[:-3]
    elif WORD_LEN > 4:
        target_word = target_word[:-2]        # у длинных слов без "ь" на конце - убираем суффикс или окончание
    elif WORD_LEN > 3:
        target_word = target_word[:-1]        # у коротких слов суффикс часто нулевой, а окончание - короткое
    # если длина слова до 3 символов включительно, то мы ничего от него не отрезаем
    return target_word


for i, row in minus_words.iterrows():       # i - индекс, row - все остальные данные в строке
    # Шаблон для поиска вхождения минус-слова в поисковой фразе. Искомое слово в фразе должно начинаться с минуса
    # 'вентилятор' != 'турбовентилятор', также слово должно быть не длиннее, чем + 3 знака: 'турбо' != 'турбонаддув'
    minus_word_reg = r'\b' + get_word_base(str(row['minus_words'])) + r'.{,3}\b'
    minus_count_dataframe = ad_stat[ad_stat['Запрос пользователя'].str.contains(minus_word_reg)]  # DataFrame с минусами
    minus_words.at[i, 'count'] = minus_count_dataframe['Показы'].sum()   # сумма показов фраз с минус-словом


minus_words.to_csv(MINUS_FILE, index=False, sep=',')    # выгружаем данные показов в исходную  таблицу минус-слов
print('Таблица минус-слов')
print(minus_words.head())

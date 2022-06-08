# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

minus_words = pd.read_csv('minus_words.csv', sep=',')  # столбцы: minus_words, count
ad_stat = pd.read_csv('ad_stat.csv', sep=';')
# столбцы SKU, Название товара, Поисковая фраза, *Запрос пользователя*, *Показы*, *?Клики, CTR (%), Расход (руб., с НДС)

print('Таблица минус-слов')
print(minus_words.head(5))
print('\n\nТаблица со статистикой')
print(ad_stat.head(5)[['Запрос пользователя', 'Показы']])
# input("Press 'Enter'")

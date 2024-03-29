## ozon-ad_minus-counter
### Подсчет количества показов по конкретным минус-словам для выбора самых важных
В рекламе OZON есть ограничение по количеству минус-слов в 100 штук. Исходя из этого есть необходимость подсчитать количество показов по каждому из собранных минус слов, чтобы в дальнейшем добавить в рекламу только самые "охватные" и таким образом отсечь максимальное количество нерелевантных платных показов рекламы.

### ВНИМАНИЕ
- При сборе минус слов, в т.ч. собираются фразы, заданные с ошибкой в раскладке ('gthtw' - вместо 'перец').
- Однако необходимо предварительно исключить фразы с русскими буквами ЁБЮХЪ, т.к. вместо них получаем `,.[]~<>{}
- Наличие этих символов "ломает" поиск подстроки в ДатаФреймах, который основан на RegEx, а кроме того функция поиска
определяет такие символы как конец слова, отчего весь алгоритм получает ошибки.

### TODO List
- [x] Открыть 2 файла в текущей папке и забрать из них данные в объекты Pandas
* файл с минусами - minus_words.csv. Получаем скачиванием из Google Таблиц - в таком случае разделителем становится ','
* файл со статистикой рекламы - ad_stat.csv. Получаем скачиванием из кабинета OZON - разделитель ';'

- Заголовки файла 'minus_words.csv'
__minus_words__, __count__

- Заголовки файла 'ad_stat.csv'
SKU, Название товара, Поисковая фраза, Запрос пользователя, Показы, Клики, CTR (%), Расход (руб., с НДС).
Из них работаем с:
__Запрос пользователя__, __Показы__, __Клики__


- [x] Подготовить RegEx команду для получения слова без учета последних 3-х символов - СДЕЛАЛ с помощью строк Python.
По такому принципу будут проверяться минус-слова из очищенной руками таблицы. Удалять последние 2-3 символа необходимо,
чтобы не учитывать словоформы (падежи и мн. ед. ч.)

- [x] Подготовить скрипт, который будет искать слово в каждом поисковом запросе второй таблицы и при наличии забирать
из этой второй таблицы количество показов по этой фразе.
__В строке поисковой фразы мы ищем слово, равное обрезанному минусу + 3 символа опционально__

- [x] Суммируем все показы во всех ячейках, связанных с искомым ключевым словом

- [x] Выводим в первую таблицу количество показов по каждому минус-слову

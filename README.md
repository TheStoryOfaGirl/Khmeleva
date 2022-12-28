# Khmeleva

### Задача 2.3.2

Скриншот - все тесты пройдены (unittests):

![image](https://user-images.githubusercontent.com/106344305/205136816-76653393-8b0c-45d2-be60-ff99e50e1e21.png)

Скриншот - все тесты пройдены (doctests):

![image](https://user-images.githubusercontent.com/106344305/205137351-2a53169b-dc25-4590-9419-91e36d9ac0c6.png)

### Задача 2.3.3

- Запустила профилизатор в PyCharm, обнаружилось, что одни из самых затратных функций - check_published (изменение формата даты) и formatting_str (очищение строки от лишних символов).

![datatime](https://user-images.githubusercontent.com/106344305/206180335-870b2830-d700-4733-8512-23dceff98b46.png)

- Попробовала осуществить изменение формата даты несколькими способами (метод check_published):
1) С использованием библиотеки dateutil

```py
def check_published(date):
   return parse(date).strftime('%d.%m.%Y')
```

- Время работы в профилизаторе:

![parse](https://user-images.githubusercontent.com/106344305/206182321-61993f1c-7b20-490b-b5f3-a946d1da65f1.png)


2) С помощью форматирования строки

```py
def check_published(date):
  date = date[:date.find('T')].split('-')
  return '.'.join(reversed(date))
```
- Время работы в профилизаторе:

![строка](https://user-images.githubusercontent.com/106344305/206182418-b38fc18c-7923-40b4-82c7-063b09e0dfc5.png)


3) C использованием библиотеки datetime (первоначальная версия)

```py
def check_published(date):
  return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y')
```
- Время работы в профилизаторе:

![datatime](https://user-images.githubusercontent.com/106344305/206182600-9885410d-164a-40bb-8f46-81794ca236ae.png)

- Оказалось, что быстрее работает второй способ, но было решено сохранить первую версию с использованием библиотеки datetime, так как читабельность кода лучше.

- Попробовала осуществить изменение метода очищения строки от лишних символов (метод formatting_str)

```py
def formatting_str(self, raw_html):
  for i in range(len(raw_html)):
      while raw_html[i].find('<') > -1:
          index1 = raw_html[i].find('<')
          index2 = raw_html[i].find('>')
          raw_html[i] = raw_html[i][:index1] + raw_html[i][index2 + 1:]
      if '\n' not in raw_html[i]:
          raw_html[i] = " ".join(raw_html[i].split())
  return raw_html
```

- Время работы в профилизаторе:

![formatting](https://user-images.githubusercontent.com/106344305/206183485-76460f7c-fda0-4cf6-853f-4e36bb18c747.png)

- Время работы в профилизаторе первоначальной версии:

![datatime](https://user-images.githubusercontent.com/106344305/206183601-34088a5e-84a2-4781-866d-0401b8523463.png)

- Оказалось, что обе версии работают примерно одинаково, поэтому было решено оставить старую версию метода.

### Задача 3.2.1
- В результате сформировались файлы по годам.

![2022-12-09](https://user-images.githubusercontent.com/106344305/206720448-a6c24c7f-9ff9-474f-8cf1-aaefadc3b37e.png)

### Задача 3.2.2

- Время работы без многопоточности:

![2022-12-11](https://user-images.githubusercontent.com/106344305/206901258-768835a1-7577-4cb7-bcb8-16ca63890164.png)

- Время работы с использованием multiprocessing:

![2022-12-11 (1)](https://user-images.githubusercontent.com/106344305/206901282-cfeb984c-c233-4863-9b3c-67168112ec99.png)

- Можно заметить, что время выполнения уменьшилось примерно на 10 секунд.

### Задача 3.2.3

- Время работы с использованием concurrent.futures(Process):

![image](https://user-images.githubusercontent.com/106344305/208094824-1a6a50e2-10d1-4d12-8101-ba2a998d8bed.png)

- В сравнении с multiprocessing данная реализация работает чуть дольше.

### Задача 3.3.1

- Частотность, с которой встречаются различные валюты:

![2022-12-19 (2)](https://user-images.githubusercontent.com/106344305/208485502-b1282d51-e216-4f1c-9c88-43cac97e7c93.png)

### Задача 3.3.2

- Сформированный csv-файл с первыми 100 профессиями

![2022-12-21](https://user-images.githubusercontent.com/106344305/208905886-b9191f3d-b5ed-4d6c-aa20-b5cf3133d96c.png)

![2022-12-21 (1)](https://user-images.githubusercontent.com/106344305/208906018-e3f4bf16-dec2-473c-ab7f-9fbbbfedabce.png)

![2022-12-21 (2)](https://user-images.githubusercontent.com/106344305/208905964-8caaf85d-ed81-49fe-b253-26166ffc1577.png)

![2022-12-21 (3)](https://user-images.githubusercontent.com/106344305/208906058-bf48326f-03b9-4f32-848e-ff3a59c55b0f.png)

### Задача 3.5.1

- Сформированная база данных с валютами

![2022-12-27](https://user-images.githubusercontent.com/106344305/209675336-a4762b97-46d6-4f91-b09f-247a0335f85c.png)

### Задача 3.5.2

- Новая таблица vacancies в базе данных currencies.db

![2022-12-28](https://user-images.githubusercontent.com/106344305/209799799-1d125f94-ecf6-419c-a6bc-032a7973dbea.png)

### Задача 3.5.3

- Код программы:

![2022-12-28 (10)](https://user-images.githubusercontent.com/106344305/209838338-fbdccbb3-9926-40bc-925c-a0fd7dd0e2b5.png)
![2022-12-28 (11)](https://user-images.githubusercontent.com/106344305/209838343-5eb0cc5c-0ffc-416b-87f1-e69a71710ff6.png)


- Результаты вывода программы:

![2022-12-28 (1)](https://user-images.githubusercontent.com/106344305/209837713-5ea0f637-d872-4513-a8cd-da037b2ed688.png)
![2022-12-28 (2)](https://user-images.githubusercontent.com/106344305/209837728-362de3a0-193e-42b2-8772-d1dcfd929337.png)
![2022-12-28 (3)](https://user-images.githubusercontent.com/106344305/209837735-8913f653-67f7-471e-9140-4f9f7cad4f74.png)
![2022-12-28 (4)](https://user-images.githubusercontent.com/106344305/209837744-92f4cf55-72a6-40b4-bcfd-b07321733c09.png)
![2022-12-28 (5)](https://user-images.githubusercontent.com/106344305/209837751-d1eadf01-6896-4a4f-b68a-137e8cbd6a03.png)
![2022-12-28 (6)](https://user-images.githubusercontent.com/106344305/209837754-530df74c-0067-46af-badf-fab780c5d4cc.png)
![2022-12-28 (7)](https://user-images.githubusercontent.com/106344305/209837756-616f209f-d755-47d8-bde5-c7797ca913b0.png)





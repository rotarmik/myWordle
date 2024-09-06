### Этот проект разработан в качестве вступительного испытания по программированию для летней школы по компьютерной обработки естественных языков (NLP). [Ссылка на сайт программы](https://letnyayashkola.org/nlp/).
Wordle - игра, в которой необходимо отгадать загаднное рандомно слово. Правила изложены ниже:

![правила игры:](https://github.com/rotarmik/myWordle/blob/main/assets/wordle_rules.PNG)
---

#### Папка src содержит:
- my_wordle.py: файл с основным кодом программы
- realisation.py: вспомогательные функции, используемые в my_wordle.py
- wordle-Ta.txt: словарь всех английских пятибуквенных слов
- words-for-guess.txt: слова, которые могут быть загаданы программой
---
#### Запуск:
```
git clone git@github.com:rotarmik/myWordle.git
cd src
```
 ##### в src:
 ```
 python my_wordle.py
 ```
![Запуск игры](https://github.com/rotarmik/myWordle/blob/main/assets/wordle.gif)

#### Требования:
- python >= 3.9
#### Библиотеки:
- numpy
- re
- os
- random

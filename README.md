# L042ATeX (LЪaTeX)

The package is a set of plugins, snippets and shotcuts for simplifying using LaTeX for users writing text in Russian. Templates and snippets targeting specially for Russian, so package will be hardly useful for other users. Russian users could begin special environments, commands, etc. using Russian layout.

## Дисклеймер
Этот пакет не для замены какого либо другого LaTeX пакета. Он предназначен для использования совместно с [LaTeXTools](https://github.com/SublimeText/LaTeXTools) и [LaTeXYZ](https://github.com/randy3k/LaTeXYZ) и возвышения процесса ввода в [Sublime Text](https://www.sublimetext.com/) до уровня комфортной погулки по давно близкому душе парку. 
Мотивацией к написанию нижеизложенного послужили непреодолимая лень автора и дихотомия ракладки клавиатуры.

Всё написанное было удобно конкретно автору написанного, так что возможна физическая боль от восприятия ниже представленной "оптимизации" процесса работы с LaTeX. Любые комментарии и предложения просьба писать [мне](https://vk.com/ka1242) (на почту тоже можно).

## Установка
Для корректной работы программы необходим пакет [Multicommand](https://packagecontrol.io/packages/Multicommand). 
Клонируйте репозиторийй в папку "..\Sublime Text 3\Packages\User" и перенесите из "L042ATeX" папки "L042ATeX.py" файл в "..\Sublime Text 3\Packages\User".
  
## Сниппеты

Есть возможность начать и закончить формулу без эксплуатации <kbd>Shift</kbd>+<kbd>Alt</kbd>, <kbd>Shift</kbd>+<kbd>Ctrl</kbd>, <kbd>Win</kbd>+<kbd>Space</kbd> и прочих бесполезных сочетаний для смены языка.

№  | Keys | Action
-----|-----|------
1 | <kbd>а</kbd>, <kbd>о</kbd> | *смена языка* **и** ```$```
2 | <kbd>Space</kbd>, <kbd>Space</kbd> | *смена языка* **и** *переход за $*

Реализована неограниченная мощь <kbd>ъ</kbd>, как намёка система для начала функционального режима. 

№  | Keys | Action
-----|-----|------
3 | <kbd>ъ</kbd>, <kbd>к</kbd> | ```\textit{}```
4 | <kbd>у</kbd>, <kbd>1</kbd> | ```$$```
4 | <kbd>у</kbd>, <kbd>2</kbd> | ```equation```
5 | <kbd>у</kbd>, <kbd>3</kbd> | ```align```
5 | <kbd>у</kbd>, <kbd>0</kbd> | ```align*```





# SkyLang

Sky, или же SkyLang/SkyScraper - язык, написанный для практики по Python. Он предоставляет базовые элементы синтаксиса, такие как объявления переменных, присваивания, условные операторы, циклы и операции ввода/вывода. Язык построен с использованием Python и использует PLY для лексического анализа и парсинга.
Некой изюминкой проекта является очень краткий синтаксис.

## Синтаксис:
```sky
v name; - VAR - Объявление переменной
v name = value; 

name = value; - присваивание значения value переменной name;

wr(); - WRITE - вывод в консоль без переноса строки

wrn(); - WRITE_NEW - вывод в консоль с переносом строки

in(); - пользовательский ввод в переменную

inn(); - пользовательский ввод числа в переменную

if () { ... } - условный оператор if

w () { ... } - WHILE - цикл "пока"
```

## Особенности

- **Лексический анализ**: Преобразует исходный код в токены, такие как операторы, ключевые слова, идентификаторы и литералы.
- **Парсинг**: Строит абстрактное синтаксическое дерево (AST) из токенов исходного кода, поддерживает арифметические операции, логические выражения, условные операторы, циклы и ввод/вывод.
- **Исполнение**: Интерпретирует программу, выполняя вычисления, управление переменными и обработку ввода/вывода.

## Синтаксис языка

### Объявления переменных

```sky
v x;        # Объявление переменной x без начального значения
v x = 10;   # Объявление переменной x с начальным значением
```
### Присваивания
```sky
x = 10;       # Присваивает переменной x значение 10
```
### Условные операторы
```sky
if (x > 5) {
    wrn(x);    # Если x больше 5, выводит значение x с переходом на новую строку
}
```
### Циклы
```sky
w (x < 10) {
    x = x + 1;  # Цикл будет выполняться, пока x меньше 10
}
```
### Ввод/Вывод
```sky
wr "Привет, мир!";  # Выводит текст без перевода строки
wrn "Привет, мир!"; # Выводит текст с переходом на новую строку
in x;               # Считывает ввод с клавиатуры и сохраняет его в переменной x
inn x;              # Считывает числовой ввод и сохраняет его в переменной x
```

```sky
v x;
inn(x);
if (x > 10) {
    wrn("Число больше 10!");
}
```

### Компоненты проекта

#### lexer.py: Лексер (токенизатор), который разбивает исходный код на токены, такие как операторы, числа, строки и ключевые слова

#### parser.py: Парсер, который строит абстрактное синтаксическое дерево (AST), применяя правила грамматики​

#### interpreter.py: Интерпретатор, который выполняет AST, выполняет вычисления, управляет переменными и взаимодействует с пользователем​

#### tokens.py: Определения токенов и ключевых слов, используемых лексером​

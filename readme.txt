Доступ к админке:

/admin/
admin
pass


Задание:

Написать веб-приложение, используя Django + SQLite + Bootstrap.
 
Через админку добавляются объекты, имеющие два поля: название и содержимое. В последнее записывается фрагмент шаблонной логики Django. 

На главной странице в шапке находится форма с выпадающим списком из названий этих объектов. При выборе одного из них, ниже выдаётся его выполненный фрагмент (т.е. не «asd|capfirst», a «Asd»).

Для демонстрации работы логики фрагмента, на страницу можно передавать какие-нибудь переменные или использовать те, что уже есть в контексте.
 
По сути это шаблоны, которые хранятся в базе.

Будет круто, но необязательно: 
- использовать AJAX для отправки формы,
- поддержка i18n в содержимом фрагмента.



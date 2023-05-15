## Текстоваый тренажер где можно выучить до 5000 тысяч английских слов в русско-английского словаря
Выполнено на Django с использованием БД SQLite   
https://ayumu.ru/

Обучение начинается с самых высокочастотных и простых слов, с постепенным расширением лексикона и добавлением всё более редких.  
Тесты идут блоками, поочерёдно выдаётся по несколько слов, сначала в англо-русском варианте ответов, затем в русско-английском.  

- слова выдаются по очереди, нужно вписать ответ и нажать enter, после ответа выдаётся следущее слово
- если предыдущий ответ не правильный, высвечивается подсказка с правильным ответом на пердыдущий вопрос
- в процессе обучения чаще работаем с теми словами, которые плохо запоминаются пока их не выучим
- если становится слишком много ошибок, новые слова перестают появлятся пока не улучшатся показатели по старым
- чередуем тренировки русско-английский и англо-русский словари блоками по несколько слов
- остановится можно в любой момент, следующая тренировка начнется с того места где вы остановились
- ответы необходимо заполнять текстом, что тренирует грамматику.
- немного статистики с количеством выученных слов, попыток ответов, % правильных ответов
- в базе 5000 английских слов

<hr>

Этот тренажер я написал прежде всего потому что хотел расширить свой лексикон и немного потренироваться писать код на python.   
По ссылке ниже вы можете посмотреть ноутбук с разбором моих успехов в расширении своего словарного запаса:  
https://github.com/VladimirSizov/study_projects_DA/blob/main/how_i_learned_english.ipynb

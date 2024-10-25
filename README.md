**Проект состоит из двух частей.**
- Первая - телеграмм-бот, которого нужно создать, запустить и убедиться в его 
работоспособности.
- Вторая - обучение моделей в каждом из заданий, сохранение их в подходящем для 
вас формате и реализация логики в боте, которая данную модель сможет 
подгружать, запускать и генерировать с помощью нее текст по заданному входному 
тексту

Ссылка на веса модели и статистики: https://disk.yandex.ru/d/b2AtjnFUW3HyUg
 
**Как устроен телеграм-бот**
1. /start старт бота. В целом можно игнорировать эту команду 
2. /model выбор модели. Нажимая на эту кнопку, предоставляется выбор модели, 
которую стоит подгрузить. После нажатия на название модели, должна 
подгрузиться соответствующая модель с параметрами генерации, после чего текст 
будет генерироваться с помощью нее. 
3. /checkmodel посмотреть название модели, какая модель сейчас загружена 
4. /generate сгенерировать текст по контексту (можно использовать без введения 
команды, просто писать текст, он будет подаваться на вход модели, модель будет 
генерировать выходной текст) 
5. /help – вывести список доступных команд

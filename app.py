from flask import Flask, request
import logging #Модуль для логгирования системной информации
import json #Модуль для записи соообщений в текстовый формат

#Запуск Фласк
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)#Будем выводить Debug сообщения,
# чтобы не пропустить любые непонятные сценарии при запуске
#
#Посылаем запрос на наш корневой адрес
@app.route("/", methods=["POST"]) #Посылаем информацию с помощью метода POST
def start():
    #выводим информацию, которая будет приходить от Алисы, это будут запросы (реквесты) в формате json
    #Json - текстовый формат обмена данными, записанный в виде "ключ": "значение"
    logging.info(request.json)
    # global end
    # end = False #Обманка, чтобы завершить диалог
    #Класс, который используется для возвращаемых ответов
    #Flask оборачивает в него данные ответа как контейнер
    #при каждом обращении к URL, добавляя необходимую информацию HTTP ответа.
    #по сути - очередная обертка для наших используемых запросов
    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False # Необходимо, чтобы не было перегрузки сессий
        }
    }



    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = "Привет! Скажи, для какого случая тебе нужна цитата?"
        #Как только получили запрос - пишем ответ!
    else:
        if req["request"]["original_utterance"].capitalize() in ["Для важных переговоров"]:
            response["response"]["text"] = "Очевидно, да вы все ######, вот что очевидно!"
        elif req["request"]["original_utterance"].capitalize() in ["Цитаты великих"]:
            response["response"]["text"] = "Стремитесь не к успеху, а к ценностям, которые он дает"
        elif req["request"]["original_utterance"].capitalize() in ["Спасибо"]:
            response["response"]["text"] = "Всего доброго! Приходите ещё!"
            response["response"]["end_session"] = True
            # end = True



    return json.dumps(response)


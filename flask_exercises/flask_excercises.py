from typing import Any, Tuple

from flask import Flask, jsonify, request

app = Flask(__name__)

flask_dict = {}


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        app.add_url_rule("/user", view_func=FlaskExercise.create, methods=["POST"])
        app.add_url_rule("/user/<username>", view_func=FlaskExercise.retrieve, methods=["GET"])
        app.add_url_rule("/user/<username>", view_func=FlaskExercise.update, methods=["PATCH"])
        app.add_url_rule("/user/<username>", view_func=FlaskExercise.delete, methods=["DELETE"])

    @staticmethod
    def create() -> tuple:
        data = request.json.get("name")
        if data:
            flask_dict[data] = dict()
            return {"data": f"User {data} is created!"}, 201
        return jsonify({"errors": {"name": "This field is required"}}), 422

    @staticmethod
    def retrieve(username: str) -> tuple:
        if username in flask_dict:
            return jsonify({"data": f"My name is {username}"}), 200
        return jsonify({"errors": "User not found"}), 404

    @staticmethod
    def update(username: str) -> tuple:
        data = request.json.get("name")
        if username in flask_dict:
            flask_dict[data] = flask_dict[username]
            del flask_dict[username]
            return {"data": f"My name is {data}"}, 200
        return jsonify({"errors": {"name": "Имя не найдено"}}), 404

    @staticmethod
    def delete(username: str) -> Tuple[Any, int]:
        if username in flask_dict:
            del flask_dict[username]
            return "", 204
        return {"errors": {"name": "Имя не найдено"}}, 404


if __name__ == "__main__":
    app.run(debug=True)

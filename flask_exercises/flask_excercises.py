from flask import Flask, make_response, Response, request


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
        database_dict: dict = {}

        def response_user_not_in_database() -> Response:
            response = make_response({"errors": "The user does not exist"}, 404)
            return response

        @app.post("/user")
        def create_user() -> Response:
            data = request.get_json()
            name = data.get("name", None)
            if name is None:
                response = make_response({"errors": {"name": "This field is required"}}, 422)
                return response
            database_dict[name] = {}
            response = make_response({"data": "User {0} is created!".format(name)}, 201)
            return response

        @app.get("/user/<username>")
        def get_user(username: str) -> Response:
            if username not in database_dict:
                response = response_user_not_in_database()
                return response
            response = make_response({"data": "My name is {0}".format(username)}, 200)
            return response

        @app.patch("/user/<username>")
        def update_user(username: str) -> Response:
            if username not in database_dict:
                response = response_user_not_in_database()
                return response
            user_data = database_dict.get(username)
            data = request.get_json()
            del database_dict[username]
            database_dict[data.get("name")] = user_data
            response = make_response({"data": "My name is {0}".format(data.get("name"))}, 200)
            return response

        @app.delete("/user/<username>")
        def delete_user(username: str) -> Response:
            if username not in database_dict:
                response = response_user_not_in_database()
                return response
            del database_dict[username]
            response = make_response({}, 204)
            return response

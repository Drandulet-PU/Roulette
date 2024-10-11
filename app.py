# Импорт библиотек
from flask import Flask
from views import register_routes

# Инициализация app
def create_app():
    DEBUG = True
    SECRET_KEY = 'development key'

    # обновляет конфиг
    app = Flask(__name__)
    app.config.from_object(__name__)

    # загружаем vies
    register_routes(app)

    return app
            
if __name__ == '__main__':
    # Запуск приложенияВ
    app = create_app()
    app.run(debug=True)
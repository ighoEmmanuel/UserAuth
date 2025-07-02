
from flask import Flask

from src.main.controller.user_controller import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix='/api')




if __name__ == '__main__':
    app.run(debug=True)

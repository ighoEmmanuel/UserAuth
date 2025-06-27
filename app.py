from flask import Flask, request

from data.model.user import User
from service.authService.login import Login
from service.authService.register import RegisterService

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    user = User(name=name, email=email, password=password)
    register_service = RegisterService(user)
    return register_service.register()



@app.route('/login',methods=['POST'])
def sign_in():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    login = Login()

    return login.login(email,password)

if __name__ == '__main__':
    app.run(debug=True)

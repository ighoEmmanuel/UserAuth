from flask import Flask, request

from data.model.blog import Blog
from data.model.user import User
from service.user_service import UserService

app = Flask(__name__)

user_service = UserService()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    user = User(name=name, email=email, password=password)
    register_service = user_service.register(user)
    return register_service



@app.route('/login',methods=['POST'])
def sign_in():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return user_service.login(email,password)


@app.route('/addPost',methods=['POST'])
def add_post():
    data = request.get_json()
    user_id = data.get('author_id')
    title = data.get('title')
    content = data.get('content')
    post = Blog(user_id, title, content)
    return user_service.add_post(post)


if __name__ == '__main__':
    app.run(debug=True)

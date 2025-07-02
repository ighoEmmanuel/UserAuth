from flask import Blueprint, request

from src.main.data.model.blog import Blog
from src.main.data.model.user import User
from src.main.service.user_service import UserService

user_controller = Blueprint('user_controller', __name__)

user_service = UserService()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    user = User(name=name, email=email, password=password)
    register_service = user_service.register(user)
    return register_service



@user_controller.route('/login',methods=['POST'])
def sign_in():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return user_service.login(email,password)


@user_controller.route('/addPost',methods=['POST'])
def add_post():
    data = request.get_json()
    user_id = data.get('author_id')
    title = data.get('title')
    content = data.get('content')
    post = Blog(user_id, title, content)
    return user_service.add_post(post)

@user_controller.route('/deletePost',methods=['PUT'])
def delete_post():
    data = request.get_json()
    blog_id = data.get('blog_id')
    return user_service.delete_post(blog_id)
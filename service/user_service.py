import re

from data.model.blog import Blog
from data.model.user import User
from data.repo.storage import Storage
from security.jwt_utils import generate_token
from security import password_hasher_and_checker
from service.blog_service import BlogService


def _is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)




class UserService:
    def __init__(self):
        self.storage = Storage()
        self.blog_service = BlogService()


    def login(self, email: str, password: str):
        user = self.storage.find_user_by_email(email)

        if user is None:
            return {"error": "User not found"}, 400

        if not password_hasher_and_checker.check_password(
            password=password,
            hashed_password=user.password
        ):
            return {"error": "Incorrect password"}, 400

        token = generate_token(user)
        return {"token": token}, 200



    def register(self,user: User):
        if not _is_valid_email(user.email):
            return {"error": "Invalid email format"}, 400

        if len(user.password) < 6:
            return {"error": "Password must be at least 6 characters long"}, 400

        if self.storage.exists_by_email(user.email):
            return {"error": "Email already exists"}, 400

        user.password = password_hasher_and_checker.hash_password(user.password)
        result = self.storage.save_user(user)
        user.id = str(result.inserted_id)
        token = generate_token(user)
        return {"token": token}, 201


    def add_post(self, post:Blog):
        user_id = post.author_id
        if self.storage.exist_by_id(user_id):
            blog_id = self.blog_service.add_blog(post)
            user = self.storage.find_user_by_id(user_id)
            user.blogs.append(blog_id)
            self.storage.update_user(user)
            return {"message": "Post added successfully"}, 200
        return {"error": "User Id  not  found"},404
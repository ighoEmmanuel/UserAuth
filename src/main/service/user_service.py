import re

from src.main.data.model.blog import Blog
from src.main.data.model.user import User
from src.main.data.repo.storage import Storage
from src.main.security.jwt_utils import generate_token
from src.main.security import password_hasher_and_checker
from src.main.service.blog_service import BlogService


def _is_valid_email(email):
    if not isinstance(email, str):
        return False
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None




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
            result  = self.blog_service.add_blog(post)
            user = self.storage.find_user_by_id(user_id)
            user.blogs.append(str(result['blog_id']))
            self.storage.update_user(user)
            return result

        return {"error": "User Id  not  found"},404

    def delete_post(self, blog_id: str):
        blog, status = self.blog_service.find_blog(blog_id)
        if status != 200:
            return blog, status

        user_id = blog["author_id"]
        self.blog_service.delete_blog(blog_id)
        user = self.storage.find_user_by_id(user_id)
        user.blogs.remove(blog_id)
        self.storage.update_user(user)
        return {"message": "Post deleted successfully"}, 200

    def get_user_blogs(self, user_id):
        user = self.storage.find_user_by_id(user_id)
        if user is None:
            return{"error": "User not found"}, 404
        return user.blogs








import re

from model.user import User
from repo.storage import Storage

from security.jwt_utils import generate_token
from service import password_hasher_and_checker


def _is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


class RegisterService:
    def __init__(self, user: User):
        self.user = user
        self.storage = Storage()

    def register(self):
        if not _is_valid_email(self.user.email):
            return {"error": "Invalid email format"}, 400

        if len(self.user.password) < 6:
            return {"error": "Password must be at least 6 characters long"}, 400

        if self.storage.exists_by_email(self.user.email):
            return {"error": "Email already exists"}, 400

        self.user.password = password_hasher_and_checker.hash_password(self.user.password)
        result = self.storage.save_user(self.user)
        self.user.id = str(result.inserted_id)
        token = generate_token(self.user)
        return {"token": token}, 201


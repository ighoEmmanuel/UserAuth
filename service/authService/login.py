from data.repo.storage import Storage
from service.authService import password_hasher_and_checker
from security.jwt_utils import generate_token

class Login:
    def __init__(self):
        self.storage = Storage()

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

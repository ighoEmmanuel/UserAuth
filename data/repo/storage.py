import os

from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask import Flask
from data.model.user import User

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URL").strip()
mongo = PyMongo(app)

class Storage:
    def __init__(self):
        self.db = mongo.db

    def save_user(self, user: User):
        user_data = user.to_dict()
        return self.db.users.insert_one(user_data)

    def find_user_by_name(self, name: str) -> User | None:
        user_data = self.db.users.find_one({"name": name})
        if user_data is None:
            return None
        return User(
                id=str(user_data["_id"]),
                name=user_data["name"],
                password=user_data["password"],
                email=user_data["email"]
        )

    def find_user_by_email(self, email: str) -> User | None:
        user_data = self.db.users.find_one({"email": email})
        if user_data is None:
            return None
        return User(
            id=str(user_data["_id"]),
            name=user_data["name"],
            password=user_data["password"],
            email=user_data["email"]
        )

    def exists_by_email(self, email: str) -> bool:
        return self.db.users.find_one({"email": email})

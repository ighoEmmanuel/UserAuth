import os
import jwt
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

from src.main.data.model.user import User

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET")


def generate_token(user: User) -> str:
    payload = {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "blogs" : user.blogs,
        "exp": (datetime.now(timezone.utc) + timedelta(hours=24)).timestamp()

    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token.decode("utf-8") if isinstance(token, bytes) else token


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def refresh_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'], options={"verify_exp": False})
        new_payload = {
            "user_id": payload["user_id"],
            "name": payload["name"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(new_payload, SECRET_KEY, algorithm='HS256')
    except jwt.InvalidTokenError:
        return None
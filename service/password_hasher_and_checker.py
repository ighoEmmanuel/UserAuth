import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')



def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
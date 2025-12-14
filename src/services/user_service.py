from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.models.user_model import User
from src.models.user_schema import UserRegister, UserLogin
from src.repositories.user_repository import (
    get_user_by_email, 
    get_user_by_username,
    create_user,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def register_user(db: Session, data: UserRegister):
    if get_user_by_email(db, data.email):
        raise ValueError("Email already exists")

    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        phone=data.phone,
        dob=data.dob,
        gender=data.gender,
        address=data.address,
    )

    return create_user(db, user)

# login
def sign_in(db: Session, data: UserLogin) -> User:
    if "@" in data.identifier:
        user = get_user_by_email(db, data.identifier)
    else:
        user = get_user_by_username(db, data.identifier)

    if not user:
        raise ValueError("Invalid credentials")

    if not verify_password(data.password, user.password):
        raise ValueError("Invalid credentials")

    return user



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.db_depend import get_db
from src.security.dependency import get_current_user
from src.models.user_schema import UserRegister, UserLogin
from src.services.user_service import register_user, sign_in
from src.security.jwt import create_access_token
from src.models.user_model import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):
    try:
        return register_user(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        user = sign_in(db, data)
        token = create_access_token(subject=user.id)
        return {
            "access_token": token,
            "token_type": "bearer",
        }
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/login/oauth")
def login_oauth(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    data = UserLogin(
        identifier=form_data.username,
        password=form_data.password
    )

    user = sign_in(db, data)
    token = create_access_token(subject=user.id)

    return {
        "access_token": token,
        "token_type": "bearer",
    }



@router.post("/logout")
def logout(user: User = Depends(get_current_user)):
    return {
        "message": "Logout successful"
    }
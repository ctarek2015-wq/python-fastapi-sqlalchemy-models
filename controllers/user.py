from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.user import UserModel
from serializers.user import UserFormSchema, UserSchema
from database import get_db

router = APIRouter()


@router.post("/register", response_model=UserSchema, status_code=201)
def create_user(user: UserFormSchema, db: Session = Depends(get_db)):

    existing_user = (
        db.query(UserModel)
        .filter((UserModel.username == user.username) | (UserModel.email == user.email))
        .first()
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    new_user = UserModel(username=user.username, email=user.email)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

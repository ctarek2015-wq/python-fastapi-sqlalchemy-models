from fastapi import APIRouter, Depends, HTTPException

# DB
from sqlalchemy.orm import Session
from database import get_db

# Models
from models.tea import TeaModel

# Serializers
from serializers.tea import TeaSchema, CreateTeaSchema, UpdateTeaSchema
from typing import List

router = APIRouter()


@router.get("/teas", response_model=List[TeaSchema])
def get_teas(db: Session = Depends(get_db)):
    teas = db.query(TeaModel).all()
    return teas

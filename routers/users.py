from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["usuarios"])

class User(BaseModel):
    id: int
    name: str
    age: int

user_list = [
    User(id=1, name="Lenin", age=46),
    User(id=2, name="Victor", age=41),
    User(id=3, name="Che", age=18),
]

@router.get("/")
async def users():
    return user_list

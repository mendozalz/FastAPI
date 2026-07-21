from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

user_list = [
    User(id=1, name="Lenin", age=46),
    User(id=2, name="Victor", age=41),
    User(id=3, name="Che", age=18),
]


@app.get("/users")
async def users():
    return user_list

def return_user_id(id:int):
    user_list_lambda = lambda user:user.id == id
    user_id = filter(user_list_lambda, user_list)
    try:
        return list(user_id)[0]
    except:
        return "Usuario no encontrado"

#Pathparams
@app.get("/user/{id}")
async def user(id:int):
    return return_user_id(id)
    

#Queryparams
@app.get("/user/")
async def user(id:int):
    return return_user_id(id)
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

def search_user_id(id:int):
    user_list_lambda = lambda user:user.id == id
    user_id = filter(user_list_lambda, user_list)
    try:
        return list(user_id)[0]
    except:
        return "Usuario no encontrado"

@app.get("/users")
async def users():
    return user_list

#Pathparams
@app.get("/user/{id}")
async def user(id:int):
    return search_user_id(id)

#Queryparams
@app.get("/user/")
async def user(id:int):
    return search_user_id(id)

############# Method Post #################

@app.post("/user/")
async def user(user: User):
    if type(search_user_id(user.id)) == User:
        return f"Error. El usuario ---{user.name}--- ya existe"
    user_list.append(user)
    return user

############# Method Put #################

@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    if not found:
        return {"Error: Usuario no actualizado"}
    return user

############# Method Delete #################

@app.delete("/user/{id}")
async def user(id:int):
    found = False
    for index, delete_user in enumerate(user_list):
        if delete_user.id == id: # Siempre verificar el ".id"
            del user_list[index]
            found = True
    if not found:
        return {"El usuario no existe"}
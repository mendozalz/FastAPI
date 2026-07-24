from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["usuario{id}"])

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


#Pathparams
@router.get("/{id}")
async def user(id:int):
    return search_user_id(id)

#Queryparams
@router.get("/")
async def user(id:int):
    return search_user_id(id)

############# Method Post #################

@router.post("/", status_code=201, description="Usuario creado exitosamente", response_model=User) # Solo en este caso se muestra el uso de Execciones HTTP ya que es a modo de estudio
async def user(user: User):
    if type(search_user_id(user.id)) == User:
        raise HTTPException(status_code=404, detail=f"El usuario ---{user.name}--- ya existe", )
        #return f"Error. El usuario ---{user.name}--- ya existe"
    user_list.routerend(user)
    return user

############# Method Put #################

@router.put("/")
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

@router.delete("/{id}")
async def user(id:int):
    found = False
    for index, delete_user in enumerate(user_list):
        if delete_user.id == id: # Siempre verificar el ".id"
            del user_list[index]
            found = True
    if not found:
        return {"El usuario no existe"}
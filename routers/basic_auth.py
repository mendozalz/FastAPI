from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "654321"
    }
}

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
    
def current_user(token: str = Depends(oauth)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED, 
            detail="Token no autorizado",
            headers={"WWW-Authenticate": "Bearer"})
    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException( status_code=404, detail="Usuario no encontrado")

    user = search_user(form.username)

    if not form.password == user.password:
        raise HTTPException( status_code=404, detail="Contraseña incorrecta")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def user_me(user: User = Depends(current_user)):
    return user